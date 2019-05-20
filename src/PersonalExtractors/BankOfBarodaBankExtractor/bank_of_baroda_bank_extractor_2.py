import re

from Utils import bsr_utils
from Utils import constants


def process_desc(json_formatted_data, desc_pattern, line):
    m = desc_pattern.match(line)
    description_extended = m.group(constants.DESCRIPTION_STR)
    json_formatted_data[constants.TRANSACTIONS_STR][-1][
        constants.DESCRIPTION_STR] += ' ' + bsr_utils.pretty_format(description_extended)


def process_transaction(json_formatted_data, line, transaction_regex, ignorable_regexes):
    transaction_pattern = re.compile(transaction_regex)
    ignorable_patterns = [re.compile(ignorable_regex) for ignorable_regex in ignorable_regexes]
    m = transaction_pattern.match(line)
    if transaction_pattern.match(line):
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
    elif bsr_utils.is_ignorable(ignorable_patterns, line):
        pass


def put_opening_balance(json_formatted_data, line):
    json_formatted_data[constants.OPENING_BALANCE_STR] = line.split()[-3]


def extract(_file, password):
    header_pattern = re.compile(constants.BOB_BANK_HEADER_REGEX)
    file_content = bsr_utils.get_file_content(_file, password)
    json_formatted_data = {
        constants.TRANSACTIONS_STR: []
    }
    transaction_pattern = re.compile(constants.BOB_BANK_TRANSACTION_REGEX)
    credit_transaction_pattern = re.compile(constants.BOB_BANK_CREDIT_TRANSACTION_REGEX)
    if file_content == 'wrongpassword':
        return 'wrongpassword'
    elif file_content == 'pdfnotreadable':
        return 'pdfnotreadable'
    for line in file_content:
        if transaction_pattern.match(line):
            m = transaction_pattern.match(line)
            if credit_transaction_pattern.match(line):
                json_formatted_data[constants.OPENING_BALANCE_STR] = bsr_utils.get_opening_bal(
                    bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR)),
                    bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)), constants.DEPOSIT_TYPE)
            else:
                json_formatted_data[constants.OPENING_BALANCE_STR] = bsr_utils.get_opening_bal(
                    bsr_utils.pretty_format(m.group(constants.CLOSING_BALANCE_STR)),
                    bsr_utils.pretty_format(m.group(constants.AMOUNT_STR)), constants.WITHDRAW_TYPE)
            break

    is_transaction_started = False
    acc_details = ''
    for line in file_content:
        if is_transaction_started:
            if "Opening Balance" in line:
                put_opening_balance(json_formatted_data, line)
            process_transaction(json_formatted_data, line, constants.BOB_BANK_TRANSACTION_REGEX_TWO,
                                constants.BOB_BANK_IGNORABLE_REGEXS)
        elif header_pattern.match(line):
            is_transaction_started = True
            bsr_utils.put_acc_details(json_formatted_data, acc_details, constants.BOB_BANK_ACCOUNT_DETAILS_REGEX_TWO)
        else:
            acc_details += line + '\n'
    return json_formatted_data
