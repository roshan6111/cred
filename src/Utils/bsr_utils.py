# operational functions
import datetime
from datetime import date
import os
from flask import Flask, current_app
import re
from Utils import constants
# from Service import ErrorCode


def put_custum_acc_details(json_formatted_data, acc_details, account_regex):
    """
    Create account details with search function
    :param json_formatted_data: where data will store
    :param acc_details: A string, with account details
    :param account_regex: regular expression
    :return:
    """
    account_pattern = re.compile(account_regex)
    m = account_pattern.search(acc_details)
    data = {}
    if m:
        for key in m.groupdict():
            data[key] = m.group(key)
    json_formatted_data.update(data)
    pretty_format_dictionary(json_formatted_data)
    print ("success")
    
def _iso_date_converter(_date):
    """
    convert date to iso format
    :param _date: A String, date
    :return: A String, iso date Format
    """
    month_in_string_flag_upper = False
    month_in_string_flag = False
    month = ''
    year = ''
    day = ''
    if '/' in _date:
        day, month, year = _date.split('/')
        if len(year) != 4:
            year = '20' + year
    elif '-' in _date:
        day, month, year = _date.split('-')
        if len(year) != 4:
            year = '20' + year
    else:
        day, month, year = _date.split(' ')
        if len(year) != 4:
            year = '20' + year
    if len(month) > 2:
        month_in_string_flag = True
        month = month.strip()
        if month.isupper():
            month_in_string_flag_upper = True
        month = date_json[month]
    else:
        month = int(month)
    year = int(year)
    day = int(day)
    if '/' in _date:
        if month_in_string_flag:
            if month_in_string_flag_upper:
                formatted_date = datetime.datetime.strptime(datetime.date(year, month, day).strftime('%d/%b/%Y'),
                                                            '%d/%b/%Y').isoformat()
            else:
                formatted_date = datetime.datetime.strptime(datetime.date(year, month, day).strftime('%d/%b/%Y'),
                                                            '%d/%b/%Y').isoformat()
        else:
            formatted_date = datetime.datetime.strptime(datetime.date(year, month, day).strftime('%d/%m/%Y'),
                                                        '%d/%m/%Y').isoformat()
    elif '-' in _date:
        if month_in_string_flag:
            if month_in_string_flag_upper:
                formatted_date = datetime.datetime.strptime(
                    datetime.date(year, month, day).strftime('%d-%b-%Y').upper(),
                    '%d-%b-%Y').isoformat()
            else:
                formatted_date = datetime.datetime.strptime(datetime.date(year, month, day).strftime('%d-%b-%Y'),
                                                            '%d-%b-%Y').isoformat()
        else:
            formatted_date = datetime.datetime.strptime(datetime.date(year, month, day).strftime('%d-%m-%Y'),
                                                        '%d-%m-%Y').isoformat()
    else:
        if month_in_string_flag:
            if month_in_string_flag_upper:
                formatted_date = datetime.datetime.strptime(
                    datetime.date(year, month, day).strftime('%d %b %Y').upper(),
                    '%d %b %Y').isoformat()
            else:
                formatted_date = datetime.datetime.strptime(datetime.date(year, month, day).strftime('%d %b %Y'),
                                                            '%d %b %Y').isoformat()
        else:
            formatted_date = datetime.datetime.strptime(datetime.date(year, month, day).strftime('%d %m %Y'),
                                                        '%d %m %Y').isoformat()
    return formatted_date


def _get_date_format(_date):
    """
    Return date format
    :param _date: A String, date
    :return: A String, date format
    """
    month_in_string_flag_upper = False
    month_in_string_flag = False
    month = ''
    year = ''
    day = ''
    if '/' in _date:
        day, month, year = _date.split('/')
        if len(year) != 4:
            year = '20' + year
    elif '-' in _date:
        day, month, year = _date.split('-')
        if len(year) != 4:
            year = '20' + year
    else:
        day, month, year = _date.split(' ')
        if len(year) != 4:
            year = '20' + year
    if len(month) > 2:
        month_in_string_flag = True
        month = month.strip()
        if month.isupper():
            month_in_string_flag_upper = True
    else:
        month = int(month)
    year = int(year)
    day = int(day)
    if '/' in _date:
        if month_in_string_flag:
            if month_in_string_flag_upper:
                return "%d/%b/%Y"
            else:
                return "%d/%b/%Y"
        else:
            return "%d/%m/%Y"
    elif '-' in _date:
        if month_in_string_flag:
            if month_in_string_flag_upper:
                return "%d-%b-%Y"
            else:
                return "%d-%b-%Y"
        else:
            return "%d-%m-%Y"
    else:
        if month_in_string_flag:
            if month_in_string_flag_upper:
                return "%d %b %Y"
            else:
                return "%d %b %Y"
        else:
            return "%d %m %Y"


def get_rev_opening_balance(idx, statement_data):
    transactions = statement_data[constants.TRANSACTIONS_STR]
    if idx == len(transactions) - 1:
        if constants.OPENING_BALANCE_STR in statement_data:
            return statement_data[constants.OPENING_BALANCE_STR]
        return 0
    return transactions[idx + 1][constants.CLOSING_BALANCE_STR]

    
def get_file_content(_file, password=None):
    """
    Convert file to text
    :param _file: A string file name
    :param password: password
    :return: file content
    """
    _file = _file.replace(" ", "")
    if password != "" and password is not None:
        response = os.system('pdftotext -layout -upw %s %s Tmp/test.txt' % (password, _file))
        if response:
            return "wrongpassword"
    else:
        response = os.system('pdftotext -layout %s Tmp/test.txt' % _file)
        if response:
            return "pdfnotreadable"
    with open('Tmp/test.txt') as f:
        content = f.readlines()
    os.system('rm -f Tmp/test.txt')
    return content

def put_acc_details(json_formatted_data, acc_details, account_regex):
    """
    Create account details with match function
    :param json_formatted_data: where data will store
    :param acc_details: A string, with account details
    :param account_regex: regular expression
    :return:
    """
    account_pattern = re.compile(account_regex)
    m = account_pattern.match(acc_details)
    data = {}
    if m:
        for key in m.groupdict():
            data[key] = m.group(key)
    json_formatted_data.update(data)
    pretty_format_dictionary(json_formatted_data)
    print ("success")

def pretty_format_dictionary(_dict):
    """
    Formate a dict:
    param _dict:
    :return:
    """
    for key in _dict:
        if not isinstance(_dict[key], str):
            continue
        _dict[key] = _dict[key].replace('\n', ' ')
        _dict[key] = re.sub('\s+', ' ', _dict[key])
        _dict[key] = _dict[key].strip()

def get_opening_balance(statement_data):
    transactions = statement_data[constants.TRANSACTIONS_STR]
    if len(transactions) == 0:
        if constants.OPENING_BALANCE_STR in statement_data:
            return statement_data[constants.OPENING_BALANCE_STR]
        return 0
    return transactions[-1][constants.CLOSING_BALANCE_STR]

def get_transaction_type(opening_bal, closing_balance):
    """
    To get Transaction type
    :param opening_bal:
    :param closing_balance:
    :return:
    """
    if float(str(opening_bal).replace(',', '')) > float(str(closing_balance).replace(',', '')):
        return constants.WITHDRAW_TYPE
    return constants.DEPOSIT_TYPE

def pretty_format(line):
    line = line.replace('\n', ' ')
    line = re.sub('\s+', ' ', line)
    return line.strip()

def is_ignorable(ignorable_patterns, line):
    """
    To find ignore string
    :param ignorable_patterns: regular expression
    :param line: A string, Description
    :return: boolean value
    """
    for ignorable_pattern in ignorable_patterns:
        if ignorable_pattern.match(line):
            return True

    return False

# def get_error_description(code):
#     """
#     Return description of code
#     :param code: A int, error code
#     :return: A string, description
#     """
#     error_description = ErrorCode.ERROR_CODE[code]
#     return error_description

def reverse_indicator(start_date, end_date):
    """
    compare the dates and find pdf reverse
    :param start_date: starting date
    :param end_date: end date
    :return: boolean value
    """
    if start_date > end_date:
        return True
    else:
        return False