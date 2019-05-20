import re

from Utils import bsr_utils, constants


# def process_desc_custum(json_formatted_data, desc_pattern, line):
#     m = desc_pattern.match(line)
#     description_extended = m.group(constants.DESCRIPTION_STR)
#     if (len(json_formatted_data[constants.TRANSACTIONS_STR]) > 0):
#         json_formatted_data[constants.TRANSACTIONS_STR][-1][constants.DESCRIPTION_STR] += ' ' + bsr_utils.pretty_format(
#             description_extended)


# def process_desc(desc_pattern, line, existing_desc):
#     m = desc_pattern.match(line)
#     existing_desc += ' ' + bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))
#     return existing_desc


def process_transaction(json_formatted_data, line, existing_desc, transaction_regex, desc_regex):
    return_statement = False
    Description_value = ''
    transaction_pattern = re.compile(transaction_regex)
    # desc_pattern = re.compile(desc_regex)
    m = transaction_pattern.match(line)
    if transaction_pattern.match(line):
        if (len(bsr_utils.pretty_format(m.group(constants.DATE_STR))) > 0) and len(
                bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))) > 0:
            Description_value = bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))
        else:
            # Description_value = existing_desc + bsr_utils.pretty_format(m.group(constants.DESCRIPTION_STR))
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

    # elif desc_pattern.match(line):
    #     if(len(json_formatted_data[constants.TRANSACTIONS_STR]) > 0):
    #         if len(json_formatted_data[constants.TRANSACTIONS_STR][-1][constants.DESCRIPTION_STR]) == 0 :
    #             print (line)
    #             process_desc_custum(json_formatted_data,desc_pattern,line)
    #         else:
    #             # print ('---line')
    #             # print (line)
    #             # print ('---dis')
    #             # print (json_formatted_data[constants.TRANSACTIONS_STR][-1][constants.DESCRIPTION_STR])
    #             existing_desc = process_desc(desc_pattern, line, existing_desc)
    #             # for back
    #     else:

    #         process_desc_custum(json_formatted_data,desc_pattern,line)

    return existing_desc


def extract(_file, password):
    header_pattern = re.compile(constants.SOUTH_INDIAN_BANK_HEADER_REGEX)
    file_content = bsr_utils.get_file_content(_file, password)
    json_formatted_data = {
        constants.TRANSACTIONS_STR: []
    }
    is_transaction_started = False
    acc_details = ''
    i = 0
    existing_desc = ''
    if file_content == 'wrongpassword':
        return 'wrongpassword'
    elif file_content == 'pdfnotreadable':
        return 'pdfnotreadable'
    while i < len(file_content):
        line = file_content[i]
        if is_transaction_started:
            existing_desc = process_transaction(json_formatted_data, line, existing_desc,
                                                constants.SOUTH_INDIAN_BANK_TRANSACTION_REGEX,
                                                constants.SOUTH_INDIAN_BANK_DESC_REGEX)
        elif header_pattern.match(line):
            is_transaction_started = True
            bsr_utils.put_acc_details(json_formatted_data, acc_details,
                                      constants.SOUTH_INDIAN_BANK_ACCOUNT_DETAILS_REGEX)
        else:
            acc_details += line + '\n'
        i = i + 1

    j = len(json_formatted_data[constants.TRANSACTIONS_STR]) - 2
    while j >= 0:
        opening_balance = bsr_utils.get_rev_opening_balance(j, json_formatted_data)
        transaction_type = bsr_utils.get_transaction_type(opening_balance,
                                                          json_formatted_data[constants.TRANSACTIONS_STR][j][
                                                              constants.CLOSING_BALANCE_STR])
        json_formatted_data[constants.TRANSACTIONS_STR][j][constants.TRANSACTION_TYPE_STR] = transaction_type
        j -= 1
    return json_formatted_data
