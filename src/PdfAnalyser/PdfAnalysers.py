
from Utils import bsr_utils
from itertools import groupby
import pydash
import json


def _monthly_emi(transaction_month_wise):
    """
    Calculate emi deposit.
    :param transaction_month_wise: A list, transaction details
    :return: A dictionary, with emi deposit
    """
    Emi_deposit = 0
    result = 0
    transaction_type = ''
    monthlyemi_list = ['EMI']
    if 'type' in transaction_month_wise[0]:
        transaction_type = 'type'
    elif 'transaction_type' in transaction_month_wise[0]:
        transaction_type = 'transaction_type'
    if transaction_type != '':
        for transaction in transaction_month_wise:
            Description = transaction['description'].upper()
            if any(y in Description for y in monthlyemi_list) and transaction[transaction_type] == 'withdraw':
                Emi_deposit += float(str(transaction['amount']).replace(',', ''))
    result = {
        "averageMonthlyEmilast2": Emi_deposit
    }
    return result

def sbi(json_data):
    count = 0
    for i in json_data['transactions']:
        date, month, year = i['date'].split(' ')
        if len(date) == 1:
            json_data['transactions'][count]['date'] = '0' + json_data['transactions'][count]['date']
        count += 1
    return json_data

def analyser(json_data, response_type):
    _name_from_extractor = ""
    _accountNo_from_extractor = ""
    if "name" in json_data:
        _name_from_extractor = json_data["name"]
    if "account" in json_data:
        _accountNo_from_extractor = json_data["account"]
    start_date = json_data['transactions'][0]['date']
    end_date = json_data['transactions'][-1]['date']
    reverse_indicator = bsr_utils.reverse_indicator(bsr_utils._iso_date_converter(start_date),
                                                    bsr_utils._iso_date_converter(end_date))

    if response_type == "STATE BANK OF INDIA":
            json_data = sbi(json_data)
    monthly_transion_grouped = {}
    durationMatch = True

    try:
        format = bsr_utils._get_date_format(start_date)
        json_data['transactions'].sort(key=lambda x: datetime.datetime.strptime(x['date'][:20], format))
    except:
        json_data['transactions'].sort(key=lambda x: x['date'][3:20])

    for groupKey, groupValue in groupby(json_data['transactions'], key=lambda x: x['date'][3:20]):
        monthly_transion_grouped[groupKey] = list(groupValue)
        if len(monthly_transion_grouped[groupKey]) < 11:
            durationMatch = False

    # arraymonth is having all month transtions in month date wise with that month total debit and total credit 
    arrayMonth = {}
    for key, value in monthly_transion_grouped.iteritems():

        # monthly emi calculator
        monthly_emi = _monthly_emi(value)
        # monthly emi calculator end

        total_debit = 0
        total_amount = 0
        total_credit = 0
        # monthly_min_value = {}

        try:

            total_debit = pydash.numerical.sum_by(value, lambda y: (
                float(str(y['amount']).replace(',', '')) if 'type' in y and y['type'] == 'withdraw' else 0))

            total_credit = pydash.numerical.sum_by(value, lambda z: (
                float(str(z['amount']).replace(',', '')) if 'type' in z and z['type'] == 'deposit' else 0))
            
            if total_debit == 0:
                total_debit = pydash.numerical.sum_by(value, lambda y: (
                    float(str(y['amount']).replace(',', '')) if 'transaction_type' in y and y[
                        'transaction_type'] == 'withdraw' else 0))

            if total_credit == 0:
                total_credit = pydash.numerical.sum_by(value, lambda z: (
                    float(str(z['amount']).replace(',', '')) if 'transaction_type' in z and z[
                        'transaction_type'] == 'deposit' else 0))

        except:
            total_debit = pydash.numerical.sum_by(value, lambda y: (
                float(str(y['amount']).replace(',', '')) if 'transaction_type' in y and y[
                    'transaction_type'] == 'withdraw' else 0))
            total_credit = pydash.numerical.sum_by(value, lambda z: (
                float(str(z['amount']).replace(',', '')) if 'transaction_type' in z and z[
                    'transaction_type'] == 'deposit' else 0))
        total_amount = pydash.numerical.sum_by(value, lambda x: float(str(x['amount']).replace(',', '')))
        format_array = {
            "month": key,
            "total_debit": total_debit,
            "total_credit": total_credit,
            "total_amount": total_amount,
            "averageMonthlyEmilast2": monthly_emi['averageMonthlyEmilast2'],
            "transactions": monthly_transion_grouped[key]
        }
        arrayMonth[key] = format_array

    return json.dumps(arrayMonth)

    return "roshan"
