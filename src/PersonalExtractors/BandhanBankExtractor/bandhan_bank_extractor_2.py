import re

from Utils import constants, bsr_utils


def process_transaction(json_formatted_data, line, existing_desc, transaction_regex, desc_regex):
    return_statement = False
    Description_value = ''
    transaction_pattern = re.compile(transaction_regex)
    m = transaction_pattern.match(line)
    if transaction_pattern.match(line):
        if (len(bsr_utils.pretty_format(m.group(constants.DATE_STR))) > 0) and len(
                bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))) > 0:
            Description_value = bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))
        else:
            Description_value = ''
            return_statement = True
        json_formatted_data[constants.TRANSACTIONS_STR].append({
            constants.DATE_STR: bsr_utils.pretty_format(m.group(constants.DATE_STR)),
            constants.DESCRIPTION_STR: Description_value,
            constants.AMOUNT_STR: bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)),
            constants.CLOSING_BALANCE_STR: bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR))
        })
        existing_desc = ''
        if return_statement:
            return existing_desc
    return existing_desc


def extract(_file, password):
    header_pattern = re.compile(constants.BANDHAN_BANK_HEADER_REGEX)
    file_content = bsr_utils.get_file_content(_file, password)
    json_formatted_data = {
        constants.TRANSACTIONS_STR: []
    }
    is_transaction_started = False
    acc_details = ''
    i = 0
    existing_desc = ''
    while i < len(file_content):
        line = file_content[i]
        if is_transaction_started:
            existing_desc = process_transaction(json_formatted_data, line, existing_desc,
                                                constants.BANDHAN_BANK_TRANSACTION_REGEX_TWO,
                                                constants.BANDHAN_BANK_DESC_REGEX)
        elif header_pattern.match(line):
            is_transaction_started = True
            bsr_utils.put_acc_details(json_formatted_data, acc_details,
                                      constants.BANDHAN_BANK_ACCOUNT_DETAILS_REGEX_TWO)
        else:
            acc_details += line + '\n'
        i = i + 1
    j = len(json_formatted_data[constants.TRANSACTIONS_STR]) - 1
    while j >= 0:
        opening_balance = bsr_utils.get_rev_opening_balance(j, json_formatted_data)
        transaction_type = bsr_utils.get_transaction_type(opening_balance,
                                                          json_formatted_data[constants.TRANSACTIONS_STR][j][
                                                              constants.CLOSING_BALANCE_STR])
        json_formatted_data[constants.TRANSACTIONS_STR][j][constants.TRANSACTION_TYPE_STR] = transaction_type
        j -= 1
    return json_formatted_data
