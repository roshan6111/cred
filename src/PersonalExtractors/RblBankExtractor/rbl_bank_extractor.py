import re

from Utils import bsr_utils
from Utils import constants


def process_desc(json_formatted_data, desc_pattern, line):
    m = desc_pattern.match(line)
    description_extended = m.group(constants.DESCRIPTION_STR)
    json_formatted_data[constants.TRANSACTIONS_STR][-1][
        constants.DESCRIPTION_STR] += ' ' + bsr_utils.pretty_format(description_extended)


def process_transaction(json_formatted_data, i, file_content, transaction_regex_1, transaction_regex_2, desc_regex,
                        ignorable_regexes):
    line = file_content[i]
    transaction_pattern_1 = re.compile(transaction_regex_1)
    transaction_pattern_2 = re.compile(transaction_regex_2)
    desc_pattern = re.compile(desc_regex)
    ignorable_patterns = [re.compile(ignorable_regex) for ignorable_regex in ignorable_regexes]
    m = transaction_pattern_1.match(line)

    if transaction_pattern_1.match(line):
        json_formatted_data[constants.TRANSACTIONS_STR].append({
            constants.DATE_STR: bsr_utils.pretty_format(m.group(constants.DATE_STR)),
            constants.DESCRIPTION_STR: bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR)),
            constants.AMOUNT_STR: bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)),
            constants.CLOSING_BALANCE_STR: bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR))
        })
    elif transaction_pattern_2.match(line):
        m = transaction_pattern_2.match(line)
        json_formatted_data[constants.TRANSACTIONS_STR].append({
            constants.DATE_STR: bsr_utils.pretty_format(m.group(constants.DATE_STR)),
            constants.DESCRIPTION_STR: bsr_utils.pretty_format(file_content[i - 1]) + ' ' + bsr_utils.pretty_format(
                m.group(constants.DESCRIPTION_STR)),
            constants.AMOUNT_STR: bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)),
            constants.CLOSING_BALANCE_STR: bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR))
        })
    elif bsr_utils.is_ignorable(ignorable_patterns, line):
        pass
    elif desc_pattern.match(line):
        process_desc(json_formatted_data, desc_pattern, line)
    # print json_formatted_data


def extract(_file, password):
    header_pattern = re.compile(constants.RBL_BANK_HEADER_REGEX)
    file_end_pattern = re.compile(constants.RBL_BANK_STATEMENT_END_REGEX)
    file_content = bsr_utils.get_file_content(_file, password)
    json_formatted_data = {
        constants.TRANSACTIONS_STR: []
    }
    is_transaction_started = False
    acc_details = ''
    i = len(file_content) - 1
    while i > 0:
        if 'Opening Balance:' in file_content[i]:
            json_formatted_data[constants.OPENING_BALANCE_STR] = file_content[i].split()[3]
            break
        i -= 1

    i = 0
    if file_content == 'wrongpassword':
        return 'wrongpassword'
    elif file_content == 'pdfnotreadable':
        return 'pdfnotreadable'
    while i < len(file_content):
        line = file_content[i]
        if file_end_pattern.match(line):
            break
        elif is_transaction_started:
            process_transaction(json_formatted_data, i, file_content, constants.RBL_BANK_TRANSACTION_REGEX_1,
                                constants.RBL_BANK_TRANSACTION_REGEX_2,
                                constants.RBL_BANK_DESC_REGEX, constants.RBL_BANK_IGNORABLE_REGEXS)
        elif header_pattern.match(line):
            is_transaction_started = True
            bsr_utils.put_acc_details(json_formatted_data, acc_details, constants.RBL_BANK_ACCOUNT_DETAILS_REGEX)
            if "name" not in json_formatted_data:
                bsr_utils.put_acc_details(json_formatted_data, acc_details,
                                          constants.RBL_BANK_ACCOUNT_DETAILS_REGEX_TWO)
        else:
            acc_details += line + '\n'
        i += 1

    j = len(json_formatted_data[constants.TRANSACTIONS_STR]) - 1
    while j >= 0:
        opening_balance = bsr_utils.get_rev_opening_balance(j, json_formatted_data)
        transaction_type = bsr_utils.get_transaction_type(opening_balance,
                                                          json_formatted_data[constants.TRANSACTIONS_STR][j][
                                                              constants.CLOSING_BALANCE_STR])
        json_formatted_data[constants.TRANSACTIONS_STR][j][constants.TRANSACTION_TYPE_STR] = transaction_type
        j -= 1
    return json_formatted_data
