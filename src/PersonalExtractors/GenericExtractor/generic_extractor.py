import re

from Utils import bsr_utils
from Utils import constants


def put_acc_details(json_formatted_data, acc_details, account_regex):
    account_pattern = re.compile(account_regex)
    m = account_pattern.match(acc_details)
    json_formatted_data.update({constants.ACCOUNT_STR: m.group(constants.ACCOUNT_STR),
                                constants.FROM_STR: m.group(constants.FROM_STR),
                                constants.TO_STR: m.group(constants.TO_STR),
                                constants.NAME_STR: m.group(constants.NAME_STR),
                                constants.ADDRESS_STR: m.group(constants.ADDRESS_STR),
                                constants.BRANCH_STR: m.group(constants.BRANCH_STR),
                                constants.BRANCH_ADDRESS_STR: m.group(constants.BRANCH_ADDRESS_STR),
                                constants.IFSC_STR: m.group(constants.IFSC_STR),
                                constants.OPENING_BALANCE_STR: m.group(constants.OPENING_BALANCE_STR)
                                })
    bsr_utils.pretty_format_dictionary(json_formatted_data)
    # print (json_formatted_data)


def is_ignorable(ignorable_patterns, line):
    for ignorable_pattern in ignorable_patterns:
        if ignorable_pattern.match(line):
            return True
    return False


def process_desc(json_formatted_data, desc_pattern, line):
    m = desc_pattern.match(line)
    groups = m.groups()
    if constants.OPENING_BALANCE_STR in groups:
        opening_balance = m.group(constants.OPENING_BALANCE_STR)
        if opening_balance != '':
            json_formatted_data[constants.TRANSACTIONS_STR][-1][
                constants.OPENING_BALANCE_STR] += bsr_utils.pretty_format(opening_balance)
    if constants.DESCRIPTION_STR in groups:
        description_extended = m.group(constants.DESCRIPTION_STR)
        if description_extended != '':
            json_formatted_data[constants.TRANSACTIONS_STR][-1][
                constants.DESCRIPTION_STR] += ' ' + bsr_utils.pretty_format(description_extended)


def process_transaction(json_formatted_data, line, transaction_regex, desc_regex, ignorable_regexes):
    transaction_pattern = re.compile(transaction_regex)
    desc_pattern = re.compile(desc_regex)
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
    elif is_ignorable(ignorable_patterns, line):
        pass
    elif desc_pattern.match(line):
        process_desc(json_formatted_data, desc_pattern, line)
    # print json_formatted_data


class GenericExtractor():
    def __init__(self):
        pass

    @staticmethod
    def extract(file, header_regex, file_end_regex, account_regex, transaction_regex, desc_regex,
                ignorable_regexes):
        header_pattern = re.compile(header_regex)
        file_end_pattern = re.compile(file_end_regex)
        file_content = bsr_utils.get_file_content(file)
        json_formatted_data = {
            constants.TRANSACTIONS_STR: []
        }
        is_transaction_started = False
        acc_details = ''
        for line in file_content:
            if file_end_pattern.match(line):
                break
            elif is_transaction_started:
                process_transaction(json_formatted_data, line, transaction_regex, desc_regex, ignorable_regexes)
            elif header_pattern.match(line):
                is_transaction_started = True
                put_acc_details(json_formatted_data, acc_details, account_regex)
            else:
                acc_details += line + '\n'
        return json_formatted_data
