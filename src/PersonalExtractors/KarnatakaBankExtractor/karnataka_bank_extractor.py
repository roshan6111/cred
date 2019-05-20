# file_line_test=open("karnataka_union_bank_extractor.txt","a+")
# file_line_test.write(line)

import re

from Utils import bsr_utils
from Utils import constants


def process_desc(json_formatted_data, desc_pattern, line):
    m = desc_pattern.match(line)
    description_extended = m.group(constants.DESCRIPTION_STR)
    if (len(json_formatted_data[constants.TRANSACTIONS_STR]) > 0):
        json_formatted_data[constants.TRANSACTIONS_STR][-1][constants.DESCRIPTION_STR] += ' ' + bsr_utils.pretty_format(
            description_extended)


def process_transaction(json_formatted_data, line, transaction_regex, desc_regex):
    transactoin_pattern = re.compile(transaction_regex)
    desc_pattern = re.compile(desc_regex)
    m = transactoin_pattern.search(line)
    if transactoin_pattern.search(line):
        opening_balance = bsr_utils.get_opening_balance(json_formatted_data)
        transaction_type = bsr_utils.get_transaction_type(opening_balance, bsr_utils.pretty_format(
            m.group(constants.CLOSING_BALANCE_STR)))
        json_formatted_data[constants.TRANSACTIONS_STR].append({
            constants.DATE_STR: bsr_utils.pretty_format(m.group(constants.DATE_STR)),
            constants.DESCRIPTION_STR: bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR)),
            constants.TYPE_STR: transaction_type,
            constants.AMOUNT_STR: bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)),
            constants.CLOSING_BALANCE_STR: bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR))
        })
    elif desc_pattern.match(line):
        process_desc(json_formatted_data, desc_pattern, line)
    # desc_regex


def put_opening_balance(json_formatted_data, line):
    json_formatted_data[constants.OPENING_BALANCE_STR] = line.split()[-1]


def extract(_file, password):
    file_end_pattern = re.compile(constants.KARNATAKA_BANK_STATEMENT_END_REGEX)
    header_pattern = re.compile(constants.KARNATAKA_BANK_HEADER_REGEX)
    file_content = bsr_utils.get_file_content(_file, password)
    json_formatted_data = {
        constants.TRANSACTIONS_STR: []
    }
    is_transaction_started = False
    acc_details = ''
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
            process_transaction(json_formatted_data, line, constants.KARNATAKA_BANK_TRANSACTION_REGEX,
                                constants.KARNATAKA_BANK_DESC_REGEX)
        elif header_pattern.match(line):
            is_transaction_started = True
            i += 2
            put_opening_balance(json_formatted_data, file_content[i])
            bsr_utils.put_custum_acc_details(json_formatted_data, acc_details,
                                             constants.KARNATAKA_BANK_ACCOUNT_DETAILS_REGEX)
        else:
            acc_details += line + '\n'
        i = i + 1
    return json_formatted_data
