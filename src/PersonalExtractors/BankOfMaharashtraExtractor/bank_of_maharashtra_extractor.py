import re

from Utils import bsr_utils
from Utils import constants


def process_desc_custum(json_formatted_data, desc_pattern, line, existing_desc):
    m = desc_pattern.match(line)
    description_extended = existing_desc + m.group(constants.DESCRIPTION_STR)
    if len(json_formatted_data[constants.TRANSACTIONS_STR]) > 0:
        json_formatted_data[constants.TRANSACTIONS_STR][-1][
            constants.DESCRIPTION_STR] += ' ' + bsr_utils.pretty_format(description_extended)


def process_transaction(json_formatted_data, i, existing_desc, transaction_regex, file_content, desc_regex,
                        ignorable_regexes):
    line = file_content[i]
    return_statement = False
    Description_value = ''
    transaction_pattern = re.compile(transaction_regex)
    desc_pattern = re.compile(desc_regex)
    ignorable_patterns = [re.compile(ignorable_regex) for ignorable_regex in ignorable_regexes]
    m = transaction_pattern.match(line)

    if transaction_pattern.match(line):
        if (len(bsr_utils.pretty_format(m.group(constants.DATE_STR))) > 0) and len(
                bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))) > 0:
            Description_value = bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))
        else:
            Description_value = ''
            return_statement = True
        opening_balance = bsr_utils.get_opening_balance(json_formatted_data)
        transaction_type = bsr_utils.get_transaction_type(opening_balance, bsr_utils.pretty_format(
            m.group(constants.CLOSING_BALANCE_STR)))
        json_formatted_data[constants.TRANSACTIONS_STR].append({
            constants.DATE_STR: bsr_utils.pretty_format(m.group(constants.DATE_STR)),
            # constants.DESCRIPTION_STR: bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR)),
            constants.DESCRIPTION_STR: Description_value,
            constants.TYPE_STR: transaction_type,
            constants.AMOUNT_STR: bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)),
            constants.CLOSING_BALANCE_STR: bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR))
        })
        if return_statement:
            return existing_desc
    elif bsr_utils.is_ignorable(ignorable_patterns, line):
        pass
    elif desc_pattern.match(line):
        if existing_desc is None or existing_desc == '':
            existing_desc = existing_desc + line
        else:
            process_desc_custum(json_formatted_data, desc_pattern, line, existing_desc)
            existing_desc = ''
    return existing_desc


def extract(_file, password):
    header_pattern = re.compile(constants.MAHARASHTRA_BANK_HEADER_REGEX)
    file_end_pattern = re.compile(constants.MAHARASHTRA_BANK_STATEMENT_END_REGEX)
    file_content = bsr_utils.get_file_content(_file, password)
    json_formatted_data = {
        constants.TRANSACTIONS_STR: []
    }
    is_transaction_started = False
    acc_details = ''
    existing_desc = ''
    i = 0
    if file_content == 'wrongpassword':
        return 'wrongpassword'
    elif file_content == 'pdfnotreadable':
        return 'pdfnotreadable'
    while i < len(file_content):
        line = file_content[i]
        if file_end_pattern.match(line):
            break
        if is_transaction_started:
            existing_desc = process_transaction(json_formatted_data, i, existing_desc,
                                                constants.MAHARASHTRA_BANK_TRANSACTION_REGEX, file_content,
                                                constants.MAHARASHTRA_BANK_DESC_REGEX,
                                                constants.MAHARASHTRA_BANK_IGNORABLE_REGEXS)
        elif header_pattern.search(line):
            is_transaction_started = True
            bsr_utils.put_acc_details(json_formatted_data, acc_details,
                                      constants.MAHARASHTRA_BANK_ACCOUNT_DETAILS_REGEX)
        else:
            acc_details += line + '\n'
        i += 1
    return json_formatted_data
