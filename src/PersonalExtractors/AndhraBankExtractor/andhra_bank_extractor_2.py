import re

from Utils import bsr_utils, constants


def process_desc(json_formatted_data, desc_pattern, line):
    m = desc_pattern.match(line)
    description_extended = m.group(constants.DESCRIPTION_STR)
    if (len(json_formatted_data[constants.TRANSACTIONS_STR]) > 0):
        json_formatted_data[constants.TRANSACTIONS_STR][-1][constants.DESCRIPTION_STR] += ' ' + bsr_utils.pretty_format(
            description_extended)


def process_transaction(json_formatted_data, line, transaction_regex, desc_regex, ignorable_regexes):
    transaction_pattern = re.compile(transaction_regex)
    desc_pattern = re.compile(desc_regex)
    ignorable_patterns = [re.compile(ignorable_regex) for ignorable_regex in ignorable_regexes]
    m = transaction_pattern.match(line)

    if transaction_pattern.match(line):
        # opening_balance = bsr_utils.get_opening_balance(json_formatted_data)
        json_formatted_data[constants.TRANSACTIONS_STR].append({
            constants.DATE_STR: bsr_utils.pretty_format(m.group(constants.DATE_STR)),
            constants.DESCRIPTION_STR: bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR)),
            constants.AMOUNT_STR: bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)),
            constants.CLOSING_BALANCE_STR: bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR))
        })
    elif bsr_utils.is_ignorable(ignorable_patterns, line):
        pass
    elif desc_pattern.match(line):
        process_desc(json_formatted_data, desc_pattern, line)


def extract(_file, password):
    header_pattern = re.compile(constants.ANDHRA_BANK_TWO_HEADER_REGEX)
    file_end_pattern = re.compile(constants.ANDHRA_BANK_STATEMENT_END_REGEX)
    file_content = bsr_utils.get_file_content(_file, password)
    json_formatted_data = {
        constants.TRANSACTIONS_STR: []
    }
    is_transaction_started = False
    acc_details = ''
    if file_content == 'wrongpassword':
        return 'wrongpassword'
    elif file_content == 'pdfnotreadable':
        return 'pdfnotreadable'
    for line in file_content:
        if file_end_pattern.match(line):
            break
        elif is_transaction_started:
            process_transaction(json_formatted_data, line, constants.ANDHRA_BANK_TWO_TRANSACTION_REGEX,
                                constants.ANDHRA_BANK_DESC_REGEX, constants.ANDHRA_BANK_IGNORABLE_REGEXS)
        elif header_pattern.match(line):
            is_transaction_started = True
            bsr_utils.put_custum_acc_details(json_formatted_data, acc_details,
                                             constants.ANDHRA_BANK_TWO_ACCOUNT_DETAILS_REGEX)
        else:
            acc_details += line + '\n'
    j = len(json_formatted_data[constants.TRANSACTIONS_STR]) - 2
    while j >= 0:
        opening_balance = bsr_utils.get_rev_opening_balance(j, json_formatted_data)
        transaction_type = bsr_utils.get_transaction_type(opening_balance,
                                                          json_formatted_data[constants.TRANSACTIONS_STR][j][
                                                              constants.CLOSING_BALANCE_STR])
        json_formatted_data[constants.TRANSACTIONS_STR][j][
            constants.TRANSACTION_TYPE_STR] = transaction_type
        j -= 1
    # print (json.dumps(json_formatted_data))
    return json_formatted_data
