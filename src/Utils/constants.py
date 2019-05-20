ACCOUNT_STR = 'account'
FROM_STR = 'from'
TO_STR = 'to'
NAME_STR = 'name'
ADDRESS_STR = 'address'
BRANCH_STR = 'branch'
BRANCH_ADDRESS_STR = 'branch_address'
IFSC_STR = 'ifsc'
OPENING_BALANCE_STR = 'opening_balance'
TRANSACTIONS_STR = 'transactions'
DEPOSIT_TYPE = 'deposit'
WITHDRAW_TYPE = 'withdraw'
DATE_STR = 'date'
DESCRIPTION_STR = 'description'
AMOUNT_STR = 'amount'
WITHDRAW_AMOUNT_STR = 'withdraw_amount'
DEPOSIT_AMOUNT_STR = 'deposit_amount'
TYPE_STR = 'type'
CLOSING_BALANCE_STR = 'closing_balance'
TRANSACTION_TYPE_STR = 'transaction_type'
VALUE_DATE_STR = 'value_date'
DESCRIPTION_STR_2 = 'deposit_2'

########################################## ANDHRA BANK CONSTANTS #######################################################
ANDHRA_BANK_ACCOUNT_DETAILS_REGEX = '\s*Account Statement of (?P<' + ACCOUNT_STR + '>\d*) from (?P<' + FROM_STR + \
                                    '>\d{2}-\d{2}-\d{4}) to (?P<' + TO_STR + '>\d{2}-\d{2}-\d{4})\s*Name\s+(?P<' \
                                    + NAME_STR + '>[\s\S\d\D\w\W]*)Address\s+(?P<' + ADDRESS_STR \
                                    + '>[\s\S\d\D\w\W]*)Branch\s+(?P<' + BRANCH_STR + \
                                    '>[\s\S\d\D\w\W]*)Branch Address\s+(?P<' + BRANCH_ADDRESS_STR + \
                                    '>[\s\S\d\D\w\W]*)IFSC Code\s+(?P<ifsc>[\s\S\d\D\w\W]*)Opening Balance\s+(?P<' + \
                                    OPENING_BALANCE_STR + '>[\d.]*)'

ANDHRA_BANK_HEADER_REGEX = '\s*Date\s*Description\s*Withdrawal\s*Deposit\s*Balance'
ANDHRA_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s+(?P<' + DESCRIPTION_STR \
                                + '>[\s\S\d\D\w\W]*)\s+(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                                CLOSING_BALANCE_STR + '>[\d,.-]+)'
ANDHRA_BANK_STATEMENT_END_REGEX = 'Note: This is a system generated report need not to be signed.'
ANDHRA_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
ANDHRA_BANK_IGNORABLE_REGEXS = ['\s*Page \d+ of \d+\s*',
                                'Date\s*and\s*Time:\s*\d{2}\/\d{2}\/\d{4}\s*[\d.]*\s*(AM|PM)\s*Page \d+ of \d+\s*']
# ANDHRA_BANK_TWO_ACCOUNT_DETAILS_REGEX = '\s*Transactions\s*History\s*Account\s*Name:\s*(?P<'+ NAME_STR +'>[\s\S\d\D\w\W]*)Address:(?P<'+ADDRESS_STR+'>[\s\S\d\D\w\W]*)City:[\s\w]+State:[\s\w:]+Statement\s*of\s*account\s*(?P<'+ACCOUNT_STR+'>\d*)\s*for\sthe\speriod\sof\s(?P<'+FROM_STR+'>(\d{2}\/\d{2}\/\d{4})|'')\s*to\s* (?P<'+TO_STR+'>(\d{2}\/\d{2}\/\d{4})|'')\s*'
ANDHRA_BANK_TWO_ACCOUNT_DETAILS_REGEX = '\s*Transactions\s*History\s*Account\s*Name:\s*(?P<' + NAME_STR + '>[\s\S\d\D\w\W]*)Address:(?P<' + ADDRESS_STR + '>[\s\S\d\D\w\W]*)City:[\s\w]+State:[\s\w:]+Statement\s*of\s*account\s*(?P<' + ACCOUNT_STR + '>\d*)\s*for\sthe\speriod\sof((\s(?P<' + FROM_STR + '>(\d{2}\/\d{2}\/\d{4}))\s*to\s*(?P<' + TO_STR + '>(\d{2}\/\d{2}\/\d{4}))\s*)|\s*)'
# testing
# ANDHRA_BANK_TWO_ACCOUNT_DETAILS_REGEX = '\s*Transactions\s*History\s*Account\s*Name:\s*(?P<'+NAME_STR+'>(\w+\s?)*\s*$)([\s\S\d\D\w\W]*|\s*)Address:(?P<'+ADDRESS_STR+'>[\s\S\d\D\w\W]*)City:[\s\w]+State:[\s\w:]+Statement\s*of\s*account\s*(?P<'+ACCOUNT_STR+'>\d*)\s*for\sthe\speriod\sof((\s(?P<'+FROM_STR+'>(\d{2}\/\d{2}\/\d{4}))\s*to\s*(?P<'+TO_STR+'>(\d{2}\/\d{2}\/\d{4}))\s*)|\s*)'
# ANDHRA_BANK_TWO_ACCOUNT_DETAILS_REGEX = '\s*Transactions\s*History\s*Account\s*Name:\s*(?P<'+NAME_STR+'>(\w+\s?)*\s*$)([\s\S\d\D\w\W]*|\s*)Address:(?P<'+ADDRESS_STR+'>[\s\S\d\D\w\W]*)City:[\s\w]+State:[\s\w:]+Statement\s*of\s*account\s*(?P<'+ACCOUNT_STR+'>\d*)\s*for\sthe\speriod\sof((\s(?P<'+FROM_STR+'>(\d{2}\/\d{2}\/\d{4}))\s*to\s*(?P<'+TO_STR+'>(\d{2}\/\d{2}\/\d{4}))\s*)|\s*)'
ANDHRA_BANK_TWO_HEADER_REGEX = '\s*Tran\s*Date\s*Cheque\s*No\s*Transaction\sDescription\s*Withdrawal\s\(INR\)\s*Deposits\s\(INR\)\s*Balance\s\(INR\)'
ANDHRA_BANK_TWO_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+(?P<' + DESCRIPTION_STR \
                                    + '>[\s\S\d\D\w\W]*)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + \
                                    CLOSING_BALANCE_STR + '>[\d,-.]+)'
########################################################################################################################

########################################## AXIS BANK CONSTANTS ########################################################
AXIS_BANK_ACCOUNT_DETAILS_REGEX = '\s*(?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)Joint Holder :[\s\S\d\D\w\W]+Statement of Axis Account No ' \
                                                         ':(?P<' + ACCOUNT_STR + '>\d+) for the period \(From : (?P<' + FROM_STR + \
                                  '>\d{2}-\d{2}-\d{4}) To : (?P<' + TO_STR + '>\d{2}-\d{2}-\d{4})\)\s*'

AXIS_BANK_HEADER_REGEX = '\s*Tran Date\s*Chq No\s*Particulars\s*Debit\s*Credit\s*Balance\s*Init'
AXIS_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s+(?P<' + DESCRIPTION_STR \
                              + '>[\s\S\d\D\w\W]*)\s+(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                              CLOSING_BALANCE_STR + '>[\d,.]+)\s+[\d.]+'
AXIS_BANK_STATEMENT_END_REGEX = '\s*TRANSACTION TOTAL\s*[\d.]+\s*[\d.]+'
AXIS_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
AXIS_BANK_IGNORABLE_REGEXS = []
########################################################################################################################

########################################## ICICI BANK CONSTANTS ########################################################
ICICI_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\d\D\w\W]+Transaction Date from\s+(?P<' + FROM_STR + \
                                   '>\d{2}/\d{2}/\d{4})\s+to\s+(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})[\s\S\d\D\w\W]+' \
                                                                                'Transactions List - (?P<' + NAME_STR + \
                                   '>[\s\S\d\D\w\W]+) - (?P<' + ACCOUNT_STR + '>\d+)'

ICICI_BANK_HEADER_REGEX = '\s*S No\.\s*Value Date\s*Transaction Date\s*Cheque Number\s*Transaction Remarks\s*' \
                          'Withdrawal Amount\s*Deposit Amount\s*Balance'
ICICI_BANK_TRANSACTION_REGEX = '[\s\S\d\D\w\W]+(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+[-\d]+\s+(?P<' + DESCRIPTION_STR \
                               + '>[\s\S\d\D\w\W]*)\s+(?P<' + WITHDRAW_AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                               DEPOSIT_AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
ICICI_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
ICICI_BANK_IGNORABLE_REGEXS = ['\s*\d+\s*\n', '\s*Page\s*\d*\s*of\s*\d*', '\s*' + NAME_STR + '\s*',
                               '\s*DATE\s*MODE\*\*\s*PARTICULARS\s*DEPOSITS\s*WITHDRAWALS\s*BALANCE\s*']
ICICI_BANK_ACCOUNT_DETAILS_REGEX_TWO = '\s*(?P<' + NAME_STR + '>[\s\S\w\W\d\D]{50})\s*Your\s*Base\s*Branch:[\s\S\w\W\d\D]*Statement\s*of Transactions\s*in\s*Savings\s*Account\s*Number: \s*(?P<' + ACCOUNT_STR + '>\d+)\s*in\s*INR\s*for\s*the\s*period\s*(?P<' + FROM_STR + '>.*)\s*-(?P<' + TO_STR + '>.*)'
ICICI_BANK_HEADER_REGEX_TWO = '\s*DATE\s*MODE\*\*\s*PARTICULARS\s*DEPOSITS\s*WITHDRAWALS\s*BALANCE\s*'
ICICI_BANK_TRANSACTION_REGEX_TWO = '\s*(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
ICICI_BANK_STATEMENT_END_REGEX = '\s*Account Related Other Information'
########################################################################################################################

########################################## YES BANK CONSTANTS #######################################################
YES_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\d\D\w\W]+Period : (?P<' + FROM_STR + '>.*) to (?P<' + TO_STR + \
                                 '>.*)[\s\S\d\D\w\W]+\n(?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)Your Branch Details :' \
                                                                          '[\s\S\d\D\w\W]+IFSC : (?P<' + IFSC_STR + \
                                 '>\w+)\s+MICR :[\s\S\d\D\w\W]+Transaction details for your ACCOUNT No\.(?P<' + ACCOUNT_STR + '>\d+) \('

YES_BANK_HEADER_REGEX = '\s*Transaction\s*Value Date\s*Description\s*Debit\s*Credit\s*Balance|\s*Value\s*Date\s*Description\s*Withdrawals\s*Deposits\s*Balance'
YES_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+\d{2}/\d{2}/\d{4}\s+(?P<' + DESCRIPTION_STR \
                             + '>[\s\S\d\D\w\W]*)\s+(?P<' + WITHDRAW_AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                             DEPOSIT_AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
YES_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
YES_BANK_IGNORABLE_REGEXS = ['\s*Transaction', '\s*Value Date\s*Description\s*Debit\s*Credit\s*Balancee',
                             '\s*Page \d+ of \d+\s*',
                             '\s*This is a system generated statement and does not require signature.', '\s*Date\s*\n',
                             '\n', '\s*Nomination:']
YES_BANK_STATEMENT_END_REGEX = '\s*Opening Balance: (?P<' + OPENING_BALANCE_STR + '>[\d.]+)\s+'
########################################################################################################################

########################################## IDBI BANK CONSTANTS ##########################################################
IDBI_BANK_ACCOUNT_DETAILS_REGEX = '\s*Primary\s*: (?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)\s*\nAccount holder' \
                                                                     '[\s\S\d\D\w\W]+Account No\s*:\s*(?P<' + \
                                  ACCOUNT_STR + '>\d+)\s*\nCustomer ID[\s\S\d\D\w\W]+Account Branch\s*:\s*(?P<' + BRANCH_STR + \
                                  '>[\s\S\d\D\w\W]*)Mode of[\s\S\d\D\w\W]*Transactions Date from (?P<' + \
                                  FROM_STR + '>.*) to (?P<' + TO_STR + '>.*)\s*A/c No\. :'

IDBI_BANK_HEADER_REGEX = '\s*Srl\s*Txn Date\s*Value Date\s*Description\s*Cheque\s*CR/DR\s*CCY\s*Trxn Amount\s*Balance'
IDBI_BANK_TRANSACTION_REGEX = '\s*\d+\s+(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{2})\s+\d{2}/\d{2}/\d{2}\s+(?P<' + DESCRIPTION_STR + '>.*)\s+(?P<' + \
                              TRANSACTION_TYPE_STR + '>(CR|DR))\s+\w+\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + \
                              CLOSING_BALANCE_STR + '>[\d,.-]+)'
IDBI_BANK_STATEMENT_END_REGEX = '\s*Statement Summary :-'
########################################################################################################################

########################################## CORPORATION BANK CONSTANTS #######################################################
CORPORATION_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S]+Account Name\s+:\s+(?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)Branch Address :' \
                                                                                       '[\s\S\d\D\w\W]+From Date[\s\S]+:[\s\S]+' \
                                                                                       '(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})[\s\S]+To Date[\s\S]+:' \
                                                                                                           '[\s\S]+(?P<' + \
                                         TO_STR + '>\d{2}/\d{2}/\d{4})[\s\S]+Txn\. Date[\s\S\d\D\w\W]+BRANCH[\s\S]+:(?P<' + BRANCH_STR + \
                                         '>[\s\S\d\D\w\W]+)/IFSC Code:(?P<' + IFSC_STR + '>[\s\S\d\D\w\W]+)/ACCOUNT NO[\s\S]+:(?P<' + \
                                         ACCOUNT_STR + '>[\s\S\d\D\w\W]+)/15[\s\S\d\D\w\W]+Opening Balance\s+(?P<' + \
                                         OPENING_BALANCE_STR + '>[\d.,]+)[\s\S\d\D\w\W]+'

CORPORATION_BANK_HEADER_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+(?P<' + DESCRIPTION_STR \
                                + '>[\s\S\d\D\w\W]+)\s+\w+\s+(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                                CLOSING_BALANCE_STR + '>[\d,.-]+)'
CORPORATION_BANK_TRANSACTION_REGEX = CORPORATION_BANK_HEADER_REGEX
CORPORATION_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
CORPORATION_BANK_IGNORABLE_REGEXS = ['\s*Corporation Bank\s+Page \d+',
                                     '\s*Txn. Date\s*Particulars\s*Chq no\.\s*Txn\.Type Withdrawal\s*Deposit\s*Balance']
CORPORATION_BANK_STATEMENT_END_REGEX = '\s*\d{2}/\d{2}/\d{4}\s+Closing Balance\s+[\d,.]+'
########################################################################################################################

########################################## DIGIBANK CONSTANTS #######################################################
DIGI_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\d\D\w\W]+digibank\n\n\s*(?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)DBS Bank Ltd' \
                                                                                    '[\s\S\d\D\w\W]+IFSC : (?P<' + \
                                  IFSC_STR + '>[\w]+)\n[\s\S\d\D\w\W]+Account Number: (?P<' + ACCOUNT_STR + \
                                  '>[\s\S\d\D\w\W]+)Account Type:[\s\S\d\D\w\W]+Statement Period: (?P<' + FROM_STR + \
                                  '>\d{2}-\w{3}-\d{4}) To (?P<' + TO_STR + '>\d{2}-\w{3}-\d{4})\s*\n[\s\S\d\D\w\W]+' \
                                                                           'Opening Balance\s+(?P<' + \
                                  OPENING_BALANCE_STR + '>[\d.,]+)'

DIGI_BANK_HEADER_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-\w{3}-\d{4})\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)' \
                                                                                                 '\s+(?P<' + AMOUNT_STR \
                         + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
DIGI_BANK_TRANSACTION_REGEX = DIGI_BANK_HEADER_REGEX
DIGI_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
DIGI_BANK_IGNORABLE_REGEXS = ['\s*\n', '\s*digibank, powered by DBS', '\s*DBS Bank Ltd,', '\s*PRIVATE & CONFIDENTIAL',
                              '\s*Account Alias Name:-', 'Account Number:', 'Statement Period:',
                              '\s*Date\s+Details of transaction']
DIGI_BANK_STATEMENT_END_REGEX = '\s*Closing Balance\s+[\d,.]+'
########################################################################################################################

########################################## CITI BANK CONSTANTS #######################################################
CITI_BANK_ACCOUNT_DETAILS_REGEX = '\s*Page 1 of \d+\s*CITIBANK.*\n\s*(?P<' + NAME_STR + '>[A-Z\s]+)\s\s\s\s[\s\S\w\W\d\D]+IFSC ' \
                                                                                        'CODE : (?P<' + IFSC_STR + \
                                  '>[\w]+)[\s\S\w\W\d\D]+Citibank Account Number: (?P<' + ACCOUNT_STR + '>\d+)[\s\S\w\W\d\D]+Statement Period: ' \
                                                                                                        '[\s\S\w\W\d\D]+For the period (?P<' + \
                                  FROM_STR + '>\d{2}-\d{2}-\d{4}) to (?P<' + TO_STR + '>\d{2}-\d{2}-\d{4})[\s\S\w\W\d\D]+Opening ' \
                                                                                      'Balance: (?P<' + \
                                  OPENING_BALANCE_STR + '>[\d.,]+)'

CITI_BANK_HEADER_REGEX = '\s*Date\s*Transaction Details\s*Withdrawals\s*Deposits\s*Balance'
CITI_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+(?P<' + DESCRIPTION_STR \
                              + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d,-.]+)\s+(?P<' + \
                              CLOSING_BALANCE_STR + '>[\d.-,]+)'
CITI_BANK_STATEMENT_END_REGEX = '\s*Final Tally'
CITI_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
CITI_BANK_IGNORABLE_REGEXS = ['\s*Page \d+ of \d+\s*', CITI_BANK_HEADER_REGEX]
########################################################################################################################

########################################## KOTAK BANK CONSTANTS ########################################################
KOTAK_BANK_ACCOUNT_DETAILS_REGEX = '(?P<' + NAME_STR + '>[A-Z.\s]+)Period\s+: (?P<' + FROM_STR + '>\d{2}-\d{2}-\d{4}) ' \
                                                                                                 'to (?P<' + TO_STR + \
                                   '>\d{2}-\d{2}-\d{4})[\s\S\w\W\d\D]+Account No\s+: (?P<' + ACCOUNT_STR + '>\d+)[\s\S\w\W\d\D]+' \
                                                                                                           'Branch\s+: ' \
                                                                                                           '(?P<' + BRANCH_STR + \
                                   '>[\s\S\d\D\w\W]+)Nominee Registered[\s\S\w\W\d\D]+B/F\s+[\d.,]+[()CrDr]+\s+' \
                                   '(?P<' + OPENING_BALANCE_STR + '>[\d.,]+)'

KOTAK_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s+(?P<' + DESCRIPTION_STR \
                               + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)[()CrDr]+\s+(?P<' + \
                               CLOSING_BALANCE_STR + '>[\d,.-]+)'

KOTAK_BANK_HEADER_REGEX = KOTAK_BANK_TRANSACTION_REGEX
KOTAK_BANK_STATEMENT_END_REGEX = '\s*Statement Summary'
KOTAK_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
KOTAK_BANK_IGNORABLE_REGEXS = ['.*']

# KOTAK_BANK_ACCOUNT_DETAILS_REGEX_TWO = '(?P<' + NAME_STR + '>[\s\S\w\W\d\D]*)\n[\s\S\w\W\d\D]*\n[\s\S\w\W\d\D]*Account\s*No\s*.\s*(?P<' + ACCOUNT_STR + '>\d+)\n[\s\S\w\W\d\D]*From\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s*To\s*(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
KOTAK_BANK_ACCOUNT_DETAILS_REGEX_TWO = '\s*Account\s*Statement\n(?P<' + NAME_STR + '>[\s\S\w\W\d\D]*)\n[\s\S\w\W\d\D]*Cust.\s*Reln.\s*No.[\s\S\w\W\d\D]*\n[\s\S\w\W\d\D]*Account\s*No\s*.\s*(?P<' + ACCOUNT_STR + '>\d+)\n[\s\S\w\W\d\D]*From\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s*To\s*(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
KOTAK_BANK_HEADER_REGEX_TWO = '\s*Sl.\sNo.\s*Date\s*Description\s*Chq\s*/\s*Ref\snumber\s*Amount\s*Dr\s*/\s*Cr\s*Balance\s*Dr\s*/\s*Cr'
KOTAK_BANK_TRANSACTION_REGEX_TWO = '\s*\d*\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+(?P<' + DESCRIPTION_STR + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s*[(CR|DR)]+\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)\s*[(CR|DR)]+'
KOTAK_BANK_STATEMENT_END_REGEX_TWO = '\s*Opening\s*balance\s*'
KOTAK_BANK_IGNORABLE_REGEXS_TWO = [KOTAK_BANK_HEADER_REGEX_TWO]
########################################################################################################################

########################################## HDFC BANK CONSTANTS #########################################################
HDFC_BANK_TWO_ACCOUNT_DETAILS_REGEX = '[\s\S\w\W\d\D]+(?P<' + NAME_STR + '>(MR|MRS)[A-Z\s]{0,40})[\s\S\w\W\d\D]+Account\s*number\s*:\s*(?P<' + ACCOUNT_STR + '>\d+)[\s\S\w\W\d\D]*Statement\s*From\s*:\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{2})\s*TO\s:\s(?P<' + TO_STR + '>\d{2}/\d{2}/\d{2})'
HDFC_BANK_TWO_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})s* (?P<' + DESCRIPTION_STR + '>.*)\s+(?P<' + WITHDRAW_AMOUNT_STR + '>[\d,.]+)\s+(?P<' + DEPOSIT_AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
HDFC_BANK_TWO_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
HDFC_BANK_TWO_IGNORABLE_REGEXS = ['\s*STATEMENT\s*SUMMARY', '\s*Generation Date\s*:\s*', '\n',
                                  '\s*HDFC\s*BANK\s*LIMITED', '\s*Closing Balance includes',
                                  '\s*Contents\s*of\s*this\s*statement\s*will\s*be\s*considered',
                                  'State\s*account\s*branch', 'HDFC\s*Bank\s*GSTIN\s*number',
                                  'Registered\s*Office\s*Address']
########################################################################################################################

HDFC_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\w\W\d\D]+(?P<' + NAME_STR + '>(MR.|MRS)[A-Z.\s]+)City\s+: [\s\S\w\W\d\D]+Account No\s+: (?P<' + \
                                  ACCOUNT_STR + '>\d+)[\s\S\w\W\d\D]+RTGS/NEFT IFSC\s+: (?P<' + IFSC_STR + \
                                  '>[\w]+)[\s\S\w\W\d\D]+From\s+: (?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s+To\s+: ' \
                                                                                     '(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
HDFC_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{2})\s+(?P<' + DESCRIPTION_STR \
                              + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
HDFC_BANK_HEADER_REGEX = '\s*Date\s*Narration\s*Chq\./Ref.No\.|\s*Date\s*Narration\s*Chq.\s*/\s*Ref\s*No.'
HDFC_BANK_STATEMENT_END_REGEX = '\s*Opening Balance\s*Dr Count\s*Cr Count\s*Debits'
HDFC_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
HDFC_BANK_IGNORABLE_REGEXS = ['.*', '\n']
########################################################################################################################

########################################## SBI BANK CONSTANTS #######################################################
SBI_BANK_ACCOUNT_DETAILS_REGEX = '\s*Account Name\s+:\s*(?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)Address\s+:[\s\S\d\D\w\W]+' \
                                                                           'Account Number\s+:\s*(?P<' + \
                                 ACCOUNT_STR + '>\d+)[\s\S\d\D\w\W]+IFS Code\s+:\s*(?P<' + IFSC_STR + \
                                 '>[\w]+)[\s\S\d\D\w\W]+Balance as on[\s\w]+:\s*(?P<' + OPENING_BALANCE_STR + \
                                 '>[\d.,]+)[\s\S\d\D\w\W]+Account Statement from (?P<' + FROM_STR + '>.*)\s+to\s+(?P<' + \
                                 TO_STR + '>.*)'

SBI_BANK_HEADER_REGEX = '\s*Txn Date\s+Value\s+Description'
SBI_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>[\d]+ [A-Za-z]+\s*\d*)\s+(?P<' + VALUE_DATE_STR + '>[\d]+ [A-Za-z]+\s*\d*)\s+(?P<' + DESCRIPTION_STR \
                             + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d,]+[\.][\d]{2})\s+(?P<' + \
                             CLOSING_BALANCE_STR + '>[\d,.-]+)'
SBI_BANK_STATEMENT_END_REGEX = '\s*Please do not share your ATM'
SBI_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
SBI_BANK_IGNORABLE_REGEXS = ['\s*Date\s+No.\s*', SBI_BANK_HEADER_REGEX]
SBI_BANK_DESC_WITH_DATE_REGEX = '\s*(?P<' + DATE_STR + '>\d{4})\s+(?P<' + VALUE_DATE_STR + '>\d{4})\s+(?P<' + DESCRIPTION_STR + '>.*)'
########################################################################################################################

########################################## PNB BANK CONSTANTS #######################################################
PNB_BANK_ACCOUNT_DETAILS_REGEX = '\s*Account Statement For Account\s*:\s*(?P<' + ACCOUNT_STR + '>\d+)[\s\S\d\D\w\W]+Account Name\s*:\s*(?P<' \
                                 + NAME_STR + '>[\s\S\d\D\w\W]+)Branch Details[\s\S\d\D\w\W]+IFSC Code\s*:\s*(?P<' + IFSC_STR + \
                                 '>[\w]+)[\s\S\d\D\w\W]+Customer Details[\s\S\d\D\w\W]+Statement Period\s*:\s*(?P<' + FROM_STR + '>.*)\s+to\s+(?P<' + \
                                 TO_STR + '>.*)[\s\S\d\D\w\W]+Transaction\s+Cheque'

PNB_BANK_HEADER_REGEX = '\s*Date\s*Number\s*'
PNB_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>((\d{2}-\d{2}-\d{4})|(\d{2}/\d{2}/\d{4})))\s+(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                             CLOSING_BALANCE_STR + '>[\d,.]+)\s*Cr\.\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
PNB_BANK_STATEMENT_END_REGEX = '\s*Unless constituent notifies the bank'
########################################################################################################################

########################################## INDUSLAND BANK CONSTANTS #######################################################
INDUSLAND_BANK_ACCOUNT_DETAILS_REGEX = '\s*(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)\s+Generation Date\s+:[\s\S\w\W\d\D]+' \
                                                              'Period\s*:\s*(?P<' + FROM_STR + '>\d{2}-[A-Za-z]{3}-\d{4})\s+To\s+(?P<' + \
                                       TO_STR + '>\d{2}-[A-Za-z]{3}-\d{4})[\s\S\d\D\w\W]+Account No\s*:\s*(?P<' + ACCOUNT_STR \
                                       + '>\d+)[\s\S\d\D\w\W]+Brought Forward\s+(?P<' + OPENING_BALANCE_STR + \
                                       '>[\d.,]+)'
INDUSLAND_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-[A-Za-z]{3}-\d{4})\s+(?P<' + DESCRIPTION_STR \
                                   + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + \
                                   CLOSING_BALANCE_STR + '>[\d.,-]+)'
INDUSLAND_BANK_HEADER_REGEX = INDUSLAND_BANK_TRANSACTION_REGEX
INDUSLAND_BANK_STATEMENT_END_REGEX = '\s*Final Tally'
INDUSLAND_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
INDUSLAND_BANK_IGNORABLE_REGEXS = ['\s*Page : ', 'The limits and effective available']
########################################################################################################################

########################################## RBL BANK CONSTANTS #######################################################
RBL_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\w\W\d\D]+Account Name\s*:(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)Home Branch\s*:' \
                                                                                    '[\s\S\w\W\d\D]+IFSC/RTGS/NEFT ' \
                                                                                    'code\s*:\s*(?P<' + IFSC_STR + \
                                 '>[\w]+)[\s\S\w\W\d\D]+Statement\s+(?P<' + ACCOUNT_STR \
                                 + '>\d+)[\s\S\w\W\d\D]+Period\s*:\s*(?P<' + FROM_STR + '>\d{4}-\d{2}-\d{2})\s+to\s+(?P<' + \
                                 TO_STR + '>\d{4}-\d{2}-\d{2})'

RBL_BANK_HEADER_REGEX = '\s*Transaction Date\s*Withdrawl Amt|\s*Date\s*Transaction\s*Details\s*Cheque\s*ID\s*Value\s*Date\s*Withdrawl\s*Deposit\sAmt\s*Balance'
RBL_BANK_TRANSACTION_REGEX_1 = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+(?P<' + DESCRIPTION_STR \
                               + '>.*)\s+\d{2}/\d{2}/\d{4}\s+(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                               CLOSING_BALANCE_STR + '>[\d,.-]+)'
RBL_BANK_TRANSACTION_REGEX_2 = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+(?P<' + DESCRIPTION_STR \
                               + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + \
                               CLOSING_BALANCE_STR + '>[\d,-.]+)'
RBL_BANK_STATEMENT_END_REGEX = '\s*Opening Balance'
RBL_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
RBL_BANK_IGNORABLE_REGEXS = ['[\s\S\w\W\d\D]+\d{2}/\d{2}/\d{4}\s*\n', '\n', '\s*Date\s*and\s*Time\s:\s',
                             '\s*Statement\s*', '\s*Summary\s*']
RBL_BANK_ACCOUNT_DETAILS_REGEX_TWO = '\s*Accountholder\sName\s*:\s*(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)Home\s*Branch\s*:\s(?P<' + BRANCH_STR + '>[\s\S\w\W\d\D]+)Customer\s*Address\s*:\s*[\s\S\w\W\d\D]*Account\s*Number\s*:\s*(?P<' + ACCOUNT_STR + '>\d+)\s*Period\s*:\s*(?P<' + FROM_STR + '>\d{4}-\d{2}-\d{2})\sto\s*(?P<' + TO_STR + '>\d{4}-\d{2}-\d{2})'
########################################################################################################################

########################################## BOB BANK CONSTANTS ##########################################################
BOB_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\w\W\d\D]+Account Name\s+(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)\s*\n*Account Number' \
                                                                                   '\s+(?P<' + ACCOUNT_STR \
                                 + '>\d+)[\s\S\w\W\d\D]+Branch Name\s+(?P<' + BRANCH_STR + \
                                 '>[\s\S\d\D\w\W]+)\s*\n*From\s+(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{2})\s+to\s+(?P<' + \
                                 TO_STR + '>\d{2}/\d{2}/\d{2})'

BOB_BANK_HEADER_REGEX = '\s*S.No\s*Date\s*Description'
BOB_BANK_TRANSACTION_REGEX = '\s*\d+\s+(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{2})\s+(?P<' + DESCRIPTION_STR \
                             + '>.*)\s+-*\s+(?P<' + AMOUNT_STR + '>[\d.,]+)\s+-*\s+(?P<' + \
                             CLOSING_BALANCE_STR + '>[\d.,-]+)\s*(Cr|'')\s+\d{2}/\d{2}/\d{2}'
BOB_BANK_CREDIT_TRANSACTION_REGEX = '\s*\d+\s+(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{2})\s+(?P<' + DESCRIPTION_STR \
                                    + '>.*)\s+-\s+(?P<' + AMOUNT_STR + '>[\d.,]+)\s+(?P<' + \
                                    CLOSING_BALANCE_STR + '>[\d.,-]+)\s+\d{2}/\d{2}/\d{2}'
BOB_BANK_IGNORABLE_REGEXS = ['\**Bank\s*of\s*Baroda\**', '\s*S.No\s*Date\s*Description']
BOB_BANK_ACCOUNT_DETAILS_REGEX_TWO = '[\s\S\w\W\d\D]*Account\s*Number\s*:\s*(?P<' + ACCOUNT_STR + '>\d+)\s*Name\s*:\s*(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)\s*Currency\s*Code[\s\S\w\W\d\D]*Branch\s*Name\s*:\s*(?P<' + BRANCH_STR + '>[\s\S\w\W\d\D]*)ACCOUNT\s*STATEMENT\s*FROM\s*(?P<' + FROM_STR + '>\d{2}-\d{2}-\d{4})\s+TO\s*(?P<' + TO_STR + '>\d{2}-\d{2}-\d{4})'
BOB_BANK_TRANSACTION_REGEX_TWO = '\s*\d+\s+(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s+(?P<' + DESCRIPTION_STR + '>.*)\s[\s-]*(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+[\s-]*(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s*Cr'
########################################################################################################################

########################################## BOI BANK CONSTANTS #######################################################
BOI_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\w\W\d\D]+Name\s*:(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)Account No\s*:\s*' \
                                                                            '(?P<' + ACCOUNT_STR \
                                 + '>\d+)[\s\S\w\W\d\D]+IFSC Code\s*:\s*(?P<' + IFSC_STR + '>[\w]+)[\s\S\w\W\d\D]+' \
                                                                                           'For the period(?P<' + FROM_STR + '>.*)\s+to\s+(?P<' + \
                                 TO_STR + '>.*)MICR Code'

BOI_BANK_HEADER_REGEX = '\s*Sl No\s*Txn Date\s*Description'
BOI_BANK_TRANSACTION_REGEX = '\s*\d+\s+(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s+(?P<' + DESCRIPTION_STR \
                             + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)'
BOI_BANK_STATEMENT_END_REGEX = '\s*Statement Generated on'
BOI_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
BOI_BANK_IGNORABLE_REGEXS = ['\s*\(in Rs\.\)', BOI_BANK_HEADER_REGEX, '\s*\n']
BOI_BANK_ACCOUNT_DETAILS_REGEX_TWO = '[\s\S\d\D\w\W]*\s*SELECTED\s*DATE\s*RANGE\s*BETWEEN\s*(?P<' + FROM_STR + '>\d{2}-\d{2}-\d{4})\s*TO\s(?P<' + TO_STR + '>\d{2}-\d{2}-\d{4}).\s*CUSTOMER\s*DETAILS\s*[\s\S\d\D\w\W]*Account\s*No\s*\s(?P<' + ACCOUNT_STR + '>[\d]*)[\s\S\d\D\w\W]*Name\s*of\s*Customer\s*(?P<' + NAME_STR + '>[\s\S\w\W\d\D]{25})'
BOI_BANK_HEADER_REGEX_TWO = '\s*Transaction\s*Instrument\s*Id\s*Narration\s*Debit\s*Credit\s*Balance\s*'
BOI_BANK_TRANSACTION_REGEX_TWO = '\s*(?P<' + DATE_STR + '>\d{2}-\w{3}-\d{4})\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)\s+(-|\s)\s*(?P<' + AMOUNT_STR + '>[\d,.-]+)\s*(-|\s)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
BOI_BANK_STATEMENT_END_REGEX_TWO = '\s*Effective\s*available\s*balance'
########################################################################################################################

########################################## CANARA BANK CONSTANTS #######################################################
CANARA_BANK_ACCOUNT_DETAILS_REGEX = '(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)\nS/O[\s\S\w\W\d\D]+Branch\s+(?P<' + BRANCH_STR + \
                                    '>.*)\s*\n*Searched by[\s\S\w\W\d\D]+(?P<' + FROM_STR + '>\d{2}-\d{2}-\d{4})\s+to\s+(?P<' + \
                                    TO_STR + '>\d{2}-\d{2}-\d{4})[\s\S\w\W\d\D]+Account Number\s+(?P<' + ACCOUNT_STR + '>\d+)[\s\S\w\W\d\D]+Balance ' \
                                                                                                                       'B/F\s+(?P<' + OPENING_BALANCE_STR + \
                                    '>[\d.,]+)'

CANARA_BANK_HEADER_REGEX = '\s*Txn Date\s*Value Date\s*Cheque No.'
CANARA_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-[A-Za-z]{3}-\d{4})\s+\d{2}:\d{2}:\d{2}\s+' \
                                                       '\d{2}-[A-Za-z]{3}-\d{4}\s+(?P<' + DESCRIPTION_STR \
                                + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + \
                                CLOSING_BALANCE_STR + '>[\d.,-]+)'
CANARA_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
CANARA_BANK_IGNORABLE_REGEXS = ['\s*Page No.']
########################################################################################################################

########################################## SCH BANK CONSTANTS #######################################################
SCH_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\w\W\d\D]+STATEMENT DATE\s*:\s*\n*\s*\n*\s*(?P<' + \
                                 TO_STR + '>\d{2} [A-Za-z]{3} \d{4})\s*\n*\s*\n*\s*\n*\s*(?P<' + NAME_STR + \
                                 '>[\s\S\w\W\d\D]+)\s*CURRENCY[\s\S\w\W\d\D]+ACCOUNT NO.\s*:' \
                                 '\s*(?P<' + ACCOUNT_STR + '>\d+)[\s\S\w\W\d\D]+IFSC\s*:\s*(?P<' + IFSC_STR + '>[\w]+)'

SCH_BANK_HEADER_REGEX = '[\s\S\w\W\d\D]+Date[\s\S\w\W\d\D]+Description\s*Cheque\s*Deposit'
SCH_BANK_TRANSACTION_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + \
                             CLOSING_BALANCE_STR + '>[\d.,-]+)\s*\n'
SCH_BANK_STATEMENT_END_REGEX = ['\s*DDA\s+\d+\s+\d+', '\s*Bank deposits are covered', '\s*TOTAL\s+', ]
SCH_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
SCH_BANK_IGNORABLE_REGEXS = ['\s*Page \d+ of \d+\s*', SCH_BANK_HEADER_REGEX, '\s*Date\s*\n']
SCH_BANK_DATE_CHANGE_REGEX = '\s*(?P<' + DATE_STR + '>\d{2} [A-Za-z]+ \d{2})\s*\d{2} [A-Za-z]+ \d{2}\s+(?P<' + \
                             DESCRIPTION_STR + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,]+)\s*\n'
########################################################################################################################

########################################## Federal BANK CONSTANTS ######################################################
FEDERAL_BANK_ACCOUNT_DETAILS_REGEX = 'CUSTOMER\sNAME\s*:(?P<' + NAME_STR + '>[\s\S\d\D\w\W]*)\n*A/C\sNO\s&\sCUST\sID\s:(?P<' + ACCOUNT_STR + '>\s[0-9X,\s]*)\nBRANCH\sNAME\s*:\s*(?P<' + BRANCH_STR + '>[\s\S\d\D\w\W]*)\nSCHEME\sNAME\s*:\s*(?P<' + TYPE_STR + '>[\s\S\d\D\w\W]*)\nCURRENCY[\s\S\w\W\d\D]+IFSC\s*:\s*(?P<' + IFSC_STR + '>[\s\S\d\D\w\W]*)Statement\s*of\s*Accounts\s*from\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s*to\s(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
FEDERAL_BANK_HEADER_REGEX = '\s*Opening\sBalance\s*Total\sWithdrawals\s*Total\s*Deposits\s*Closing\sBalance'
FEDERAL_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)\s'
FEDERAL_BANK_STATEMENT_END_REGEX = '\s*Closing\s*Balance\s*[\d.]+'
FEDERAL_BANK_IGNORABLE_REGEXS = ['\sCUSTOMER\sNAME.', '\s*A/C\sNO\s&\sCUST\sID.', 'BRANCH\sNAME.', 'SCHEME\sNAME\s.',
                                 'CURRENCY.', 'IFSC.', '\s*Statement\s*of\s*Accounts\s*from\s.', '\s*Tran\s*Date.',
                                 '\s*Opening\sBalance.']
FEDERAL_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>.*)'
FEDERAL_BANK_ACCOUNT_DETAILS_REGEX_TWO = '\s*Name\s*:\s*(?P<' + NAME_STR + '>[\s\S\d\D\w\W]*)\s*Branch\s*Name\s*:\s*(?P<' + BRANCH_STR + '>[\s\S\d\D\w\W]*)\s*Communication\s*Address\s*:\s*[\s\S\d\D\w\W]*Account\s*Number\s*:\s*(?P<' + ACCOUNT_STR + '>[\dXx]*)[\s\S\d\D\w\W]*Statement\s*of\s*Account\s*for\sthe\s*period\s(?P<' + FROM_STR + '>.*)to(?P<' + TO_STR + '>.*)'
FEDERAL_BANK_HEADER_REGEX_TWO = '\s*Date\s*Value\sDate\s*Particulars\s*Cheque\s*Details\s*Withdrawals\s*Deposits\s*Balance\s*'
FEDERAL_BANK_STATEMENT_END_REGEX_TWO = '\s*GRAND\s*TOTAL'
########################################################################################################################

########################################## United BANK CONSTANTS #######################################################
UNITED_BANK_HEADER_REGEX = '\s*SN\s*Txn\s*Date\s*Description\s*Instr\s*No.\s*Withdrawals\s*Deposits\s*Balance'
UNITED_BANK_STATEMENT_END_REGEX = '\s*Closing\s*Balance\s*[\d.]+'
UNITED_BANK_ACCOUNT_DETAILS_REGEX = '\s*Account\s*Number:\s*(?P<' + ACCOUNT_STR + '>\d+)\s*Customer\s*Name:(?P<' + NAME_STR + '>[\s\S\w\W\d\D]+)\s*Address:[\s\S\d\D\w\W]*Transactions\s*in\s*dates\s*ranging\s*from\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s*to\s(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
UNITED_BANK_TRANSACTION_REGEX = '\s*\d\s*(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
UNITED_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
########################################################################################################################

########################################## Central BANK CONSTANTS ######################################################
CENTRAL_BANK_HEADER_REGEX = '\s*Post\s*Date\s*Value[\s\w\d\W]*Branch[\s\w\d\W]*\s*Cheque\s*Account[\s\w\d\W]*Debit\s*Credit\s*Balance'
CENTRAL_BANK_STATEMENT_END_REGEX = '\s*\*\s*Statement\s*Downloaded\s*By'
CENTRAL_BANK_ACCOUNT_DETAILS_REGEX = '[\s\w\d\W]*Account\sNumber\s*:(?P<' + ACCOUNT_STR + '>\s[\d]*)\s*Product\stype\s:\s[\w-]*\s*(?P<' + NAME_STR + '>[a-zA-Z ]+)(?P<' + ADDRESS_STR + '>[\s\w\W\d]*)Email[\s\w\W\d]*STATEMENT\s*OF\s*ACCOUNT\s*from\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s*to\s(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
CENTRAL_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})+\s*\d{2}/\d{2}/\d{4}\s*[\d\s]*(?P<' + DESCRIPTION_STR + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s*'
CENTRAL_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
########################################################################################################################

########################################## Citi Union BANK CONSTANTS ###################################################
CITI_UNION_BANK_HEADER_REGEX = '\s*DATE\s*DESCRIPTION\s*CHEQUE\s*NO\s*DEBIT\s*CREDIT\s*BALANCE'
CITI_UNION_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\w\W\d\D]+ACCOUNT\s*\NO\(15\s*DIGIT\):(?P<' + ACCOUNT_STR + '>\d+)\s*IFSC\s*:\s*(?P<' + IFSC_STR + '>[\w]+)\s*ACCOUNT\s*TYPE\s*:\s*(?P<' + TYPE_STR + '>[\s\S\d\D\w\W]*)CUSTOMER\sDETAILS\s*:\s*(?P<' + ADDRESS_STR + '>[\s\S\w\W\d\D]+)Statement[\s\S\w\W\d\D]+STATEMENT\s*OF\s*ACCOUNT\s*from\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s*to\s*(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
CITI_UNION_BANK_STATEMENT_END_REGEX = '\s*TOTAL\s*'
CITI_UNION_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})+\s*(?P<' + DESCRIPTION_STR + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s*\n'
CITI_UNION_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
########################################################################################################################

########################################## KARNATAKA BANK CONSTANTS ####################################################
KARNATAKA_BANK_HEADER_REGEX = '\s*Date\s*Particulars\s*Chq.\s*No.\s*Withdrawals\s*Deposits\s*Balance'
KARNATAKA_BANK_ACCOUNT_DETAILS_REGEX = '\s*Statement\s*for\s*A\/c\s*(?P<' + ACCOUNT_STR + '>\d*)\s*Between\s*(?P<' + FROM_STR + '>\d{2}-\d{2}-\d{4})\s*and\s*(?P<' + TO_STR + '>\d{2}-\d{2}-\d{4})[\s\d\S\W\w\D]*Name\s*:(?P<' + NAME_STR + '>[\s\S\w\W\d\D]*?)\s*Branch\s*Name\s*:\s*(?P<' + BRANCH_STR + '>[\s\S\w\W\d\D]*?)\sAddress\s*:\s*(?P<' + ADDRESS_STR + '>[\s\S\w\W\d\D]*)\s*Address'
KARNATAKA_BANK_STATEMENT_END_REGEX = '\s*Closing\s*Balance'
KARNATAKA_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})+\s*(?P<' + DESCRIPTION_STR + '>.*)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s*\n'
KARNATAKA_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
########################################################################################################################

########################################## BANDHAN BANK CONSTANTS ######################################################
BANDHAN_BANK_HEADER_REGEX = '\s*Date\s*Effective\s*Reference\s*Branch\s*Code\s*Description\s*Withdrawal\s*Deposit\sAmt.\s*Balance|\s*Date\s*Description\s*Debit/Credit\s*Amount\s*'
BANDHAN_BANK_STATEMENT_END_REGEX = '\s*Opening\s*Balance\s*Dr\s*Count\s*Cr\s*Count\s*Debits\s*Credits\s*Closing\s*Balance'
BANDHAN_BANK_ACCOUNT_DETAILS_REGEX = '\s*Name:\s*(?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)Account\s*Number\s*:\s*(?P<' + ACCOUNT_STR + '>\d+)\s*Address:\s*(?P<' + ADDRESS_STR + '>[\s\S\w\W\d\D]+)\s*Branch\s*of\sOwnership[\s\S\w\W\d\D]+Statement\s*of\s*Account\s*for\s*the\s*period\s*(?P<' + FROM_STR + '>\d{2}\/\d{2}\/\d{4})\s*to\s*(?P<' + TO_STR + '>\d{2}\/\d{2}\/\d{4})'
BANDHAN_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
# BANDHAN_BANK_TRANSACTION_REGEX = '\s*(?P<'+DATE_STR+'>\d{2}/\d{2}/\d{4})\s*\d{2}/\d{2}/\d{4}\s*[\d\s]*(?P<'+DESCRIPTION_STR+'>.*)\s+(?P<'+AMOUNT_STR+'>[\d.,-]+)\s+(?P<'+CLOSING_BALANCE_STR+'>[\d.,-]+)\s*'
BANDHAN_BANK_IGNORABLE_REGEXS = 'nothing'
BANDHAN_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s*((\d{2}/\d{2}/\d{4})|\d)\s*[\d\s]*(?P<' + DESCRIPTION_STR + '>.*?)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s*'
BANDHAN_BANK_ACCOUNT_DETAILS_REGEX_TWO = '[\s\S\w\W\d\D]*Name\s*:(?P<' + NAME_STR + '>[a-zA-Z\s]*)\s*Branch\s*Name\s*:(?P<' + BRANCH_STR + '>[\s\S\d\D\w\W]*)\s*Address\s*:\s*[\s\S\w\W\d\D]*Branch\s*Address\s*[\s\S\w\W\d\D]*Account\s*Number\s*:\s* (?P<' + ACCOUNT_STR + '>\d*)[\s\S\w\W\d\D]*Opening\sBalance\s*:\s*(?P<' + OPENING_BALANCE_STR + '>[\d.,-]+)\s*Closing\s*Balance\s*:\s*(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)'
BANDHAN_BANK_TRANSACTION_REGEX_TWO = '\s*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s*(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)(Dr|Cr|DR|CR)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s*'
########################################################################################################################

########################################## INDIAN OVERSEAS BANK CONSTANTS ######################################################
INDIAN_OVERSEAS_BANK_HEADER_REGEX = '\s*DATE\s*CHQ\s*NARATION\s*COD\s*DEBIT\s*CREDIT\s*BALANCE'
# INDIAN_OVERSEAS_BANK_ACCOUNT_DETAILS_REGEX = '\s*(?P<'+ACCOUNT_STR+'>[\d]{10,})\s(?P<'+NAME_STR+'>\S+((?!\s{2}).)*)\s*(.+)\sCustomer\sId\s:[\S\s]*Statement\s*for\s*the\s*period\s*from\s*(?P<'+FROM_STR+'>\d{2}/\d{2}/\d{4})\s*to\s*(?P<'+TO_STR+'>\d{2}/\d{2}/\d{4})'
INDIAN_OVERSEAS_BANK_ACCOUNT_DETAILS_REGEX = '(?P<' + ACCOUNT_STR + '>[\d]{10,})\s(?P<' + NAME_STR + '>\S+((?!\s{2}).)*)\s*(.+)\s*Customer\s*Id\s:[\S\s]*Statement\s*for\s*the\s*period\s*from\s*(?P<' + FROM_STR + '>\d{2}/\d{2}/\d{4})\s*to\s*(?P<' + TO_STR + '>\d{2}/\d{2}/\d{4})'
INDIAN_OVERSEAS_BANK_STATEMENT_END_REGEX = '.*denotes\s*cancelled\s*transaction'
INDIAN_OVERSEAS_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
INDIAN_OVERSEAS_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-\w{3}-\d{4})\s*(?P<' + DESCRIPTION_STR + '>.+)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s'
###############################################################################################################################


########################################## SOUTH INDIAN BANK CONSTANTS #######################################################
SOUTH_INDIAN_BANK_HEADER_REGEX = '\s*No.\s*Date\s*Particulars\s*Cheque\s*No.\s*Withdrawals\s*Deposits\s*Balance'
SOUTH_INDIAN_BANK_ACCOUNT_DETAILS_REGEX = '\s*Name\s*:\s*(?P<' + NAME_STR + '>[\s\S\d\D\w\W]+)Account\s*No.\s*:\s*(?P<' + ACCOUNT_STR + '>\d+)\s*Statement\s*Date\s*:\s*\d{2}/\d{2}/\d{4}\s*From\s*Date\s*:\s*(?P<' + FROM_STR + '>\d{2}\/\d{2}\/\d{4})\s*To\s*Date\s*:\s*(?P<' + TO_STR + '>\d{2}\/\d{2}\/\d{4})'
SOUTH_INDIAN_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\w\W\d\D]+)'
SOUTH_INDIAN_BANK_TRANSACTION_REGEX = '.*(?P<' + DATE_STR + '>\d{2}/\d{2}/\d{4})\s*(?P<' + DESCRIPTION_STR + '>.+?)\s+(?P<' + AMOUNT_STR + '>[\d.,-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]+)\s'
################################################################################################################################


##########################################Karur Vysya Bank CONSTANTS ###########################################################
# KARUR_VYSYA_BANK_ACCOUNT_DETAILS_REGEX ='.*Account\s*Name\s*(?P<'+NAME_STR+'>[a-zA-Z\s]*)\s*Account\s*Number\s*(?P<'+ACCOUNT_STR+'>[\d]*)\s*Branch\s*(?P<'+BRANCH_STR+'>[\s\S\d\D\w\W]*)Opening\s*Balance\s\(\s*Balance\s*B/F\s*\)\s*(?P<'+OPENING_BALANCE_STR+'>[\d,.]*)\s*Closing\s*Balance\s*(?P<'+CLOSING_BALANCE_STR+'>[\d.,]*)\s*[\d\W\w\s\S]*From\s*Date\s*(?P<'+FROM_STR+'>\d{2}-\w{3}-\d{4})\s*To\s*Date\s*(?P<'+TO_STR+'>\d{2}-\w{3}-\d{4})'
KARUR_VYSYA_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\d\D\w\W]*Account\s*Name\s*(?P<' + NAME_STR + '>[a-zA-Z\s]*)\s*Account\s*Number\s*(?P<' + ACCOUNT_STR + '>[\d]*)\s*Branch\s*(?P<' + BRANCH_STR + '>[\s\S\d\D\w\W]*)\s*Customer\s*Id[\s\S\d\D\w\W]*Opening\s*Balance\s\(\s*Balance\s*B/F\s*\)\s*(?P<' + OPENING_BALANCE_STR + '>[\d,.-]*)\s*Closing\s*Balance\s*(?P<' + CLOSING_BALANCE_STR + '>[\d.,-]*)\s*[\d\W\w\s\S]*From\s*Date\s*(?P<' + FROM_STR + '>\d{2}-\w{3}-\d{4})\s*To\s*Date\s*(?P<' + TO_STR + '>\d{2}-\w{3}-\d{4})'
KARUR_VYSYA_BANK_HEADER_REGEX = '\s*Transaction\sDate\s*Value\sDate\s*Branch\s*Cheque\s*No\s*Description\s*Debit\s*Credit\s*Balance'
KARUR_VYSYA_BANK_TRANSACTION_REGEX = '.*(?P<' + DATE_STR + '>\d{2}-\d{2}-\d{4})\s*\d{2}:\d{2}:\d{2}\s*\d{2}-\w{3}-\d{4}\s*(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)\s(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
KARUR_VYSYA_BANK_STATEMENT_END_REGEX = '\s*Note\s*:-\s*'
KARUR_VYSYA_BANK_IGNORABLE_REGEXS = ['\s*Page\s*No\s*.']
KARUR_VYSYA_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
################################################################################################################################

##########################################Syndicate Bank CONSTANTS #############################################################
SYNDICATE_BANK_HEADER_REGEX = '/*Transaction\s*Date\s*Value\sDate\s*Cheque\sNo.\s*Description\s*Debit\s*Credit\s*Balance'
SYNDICATE_BANK_ACCOUNT_DETAILS_REGEX = '\s*Customer\s*Name\s*(?P<' + NAME_STR + '>[a-zA-Z\s]*)Branch(?P<' + BRANCH_STR + '>[\s\S\d\D\w\W]*)Searched\s*By[\s\S\d\D\w\W]*Account\s*Number\s*(?P<' + ACCOUNT_STR + '>\d*)[\s\S\d\D\w\W]*Opening\s*Balance\s*(?P<' + OPENING_BALANCE_STR + '>[\d,.-]*)\s*Closing\s*Balance\s*(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]*)'
SYNDICATE_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}-\w{3}-\d{4})\s+\d{2}-\w{3}-\d{4}\s*(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)\s+(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
SYNDICATE_BANK_IGNORABLE_REGEXS = ['\s*Page\s*No\s*.']
################################################################################################################################

########################################## BANK OF MAHARASHTRA CONSTANTS ###########################################################
MAHARASHTRA_BANK_HEADER_REGEX = '\s*Date\s*Type\s*Particulars\s*Cheque\/Reference\s*No\s*Debit\s*Credit\s*Balance\s*Channel'
MAHARASHTRA_BANK_ACCOUNT_DETAILS_REGEX = '\s*User\s*Details\s*Branch\s*&\s*Account\sDetails\s*(?P<' + NAME_STR + '>[a-zA-Z\s.]*)\s*Branch\s*No\s*:\s*[\s\S\d\D\w\W]*Account\s*No\s*:\s*[\s\S\d\D\w\W]*Statement\s*for\s*Account\s*No\s*(?P<' + ACCOUNT_STR + '>[\d]*)\s*from\s*(?P<' + FROM_STR + '>\d{2}\/\d{2}\/\d{4})\s*to\s*(?P<' + TO_STR + '>\d{2}\/\d{2}\/\d{4})'
MAHARASHTRA_BANK_TRANSACTION_REGEX = '.*(?P<' + DATE_STR + '>\d{2}\/\d{2}\/\d{4})\s*(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)\s(?P<' + AMOUNT_STR + '>[\d,.]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.]+)\s*(?P<' + DESCRIPTION_STR_2 + '>[\s\S\d\D\w\W]+)'
MAHARASHTRA_BANK_IGNORABLE_REGEXS = [
    '\s*Date\s*Type\s*Particulars\s*Cheque\/Reference\s*No\s*Debit\s*Credit\s*Balance\s*Channel',
    '.*Statement\s*for\s*Account\s*No\s*[\d]*\s*from\s*\d{2}\/\d{2}\/\d{4}\s*to\s*\d{2}\/\d{2}\/\d{4}',
    '\s*Page\s*[\d]*\s*of\s*[\d]*', '\*\s*All\s*the\s*amounts\s*in\s*the\s*Statement\s*are\s*in\s*INR.',
    '\*\sUnless a constituent notifies the Bank immediately of any discrepancy found by him/her in this statement of a/c, it will be taken that he has found the a/c correct.',
    '\*\s* The Summary is on the next page.', '\*\s* END OF STATEMENT - from Internet Banking.']
MAHARASHTRA_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
MAHARASHTRA_BANK_STATEMENT_END_REGEX = '\*\s*All\s*the\s*amounts\s*in\s*the\s*Statement\s*are\s*in\s*INR.'
####################################################################################################################################

########################################## UNION BANK CONSTANTS ####################################################################
UNION_BANK_ACCOUNT_DETAILS_REGEX = '\s*Statement\s*of\s*Account\s*(?P<' + NAME_STR + '>[a-zA-Z\s.]*)Union\s*Bank\s*of\s*India\s*[\s\S\d\D\w\W]*Branch\s*(?P<' + BRANCH_STR + '>[\s\S\d\D\w\W]*)Customer\s*Id\s*[\s\S\d\D\w\W]*Account\s*No\s*(?P<' + ACCOUNT_STR + '>[\d]*)\s*State\s'
UNION_BANK_HEADER_REGEX = '\s*Date\s*Remarks\s*Tran Id\s*UTR Number\s*Instr.\s*ID\s*Withdrawals\s*Deposits\s*Balance'
UNION_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}\/\d{2}\/\d{4})\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
UNION_BANK_IGNORABLE_REGEXS = ['\s*Page\sNo', '\s*For\s*any\s*queries,', '\s*This\s*is\s*a\ssystem\sgenerated']
UNION_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
####################################################################################################################################

########################################## ALLAHABAD BANK CONSTANTS ################################################################
ALLAHABAD_BANK_HEADER_REGEX = '\s*Post\s*Date\s*Value\s*Description\s*DR\s*CR\s*Balance\s*'
ALLAHABAD_BANK_ACCOUNT_DETAILS_REGEX = '[\s\S\d\D\w\W]*IFSC\s*Code\s*:\s*(?P<' + IFSC_STR + '>\w*)\s*Account\s*Number\s:\s*(?P<' + ACCOUNT_STR + '>\d+)\s*Product\s*type\s:\s*\w*\s*(?P<' + NAME_STR + '>(Mr.|MRS|Mr|MR.|Mr|Mrs)[A-Z.\s]*)\s*[\s\S\w\W\d\D]+STATEMENT\s*OF\s*ACCOUNT\s*from\s*(?P<' + FROM_STR + '>\d{2}\/\d{2}\/\d{4})\s*to\s*(?P<' + TO_STR + '>\d{2}\/\d{2}\/\d{4})'
ALLAHABAD_BANK_STATEMENT_END_REGEX = '\s*Total\s*[\d,.]+\s*[\d,.]+'
ALLAHABAD_BANK_TRANSACTION_REGEX = '\s*(?P<' + DATE_STR + '>\d{2}\/\d{2}\/\d{4})\s+(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]+)\s+(?P<' + AMOUNT_STR + '>[\d,.-]+)\s+(?P<' + CLOSING_BALANCE_STR + '>[\d,.-]+)'
ALLAHABAD_BANK_DESC_REGEX = '(?P<' + DESCRIPTION_STR + '>[\s\S\d\D\w\W]*)'
ALLAHABAD_BANK_IGNORABLE_REGEXS = ['\s*Post\s*Date\s*Value\s*Description\s*DR\s*CR\s*Balance\s*']
####################################################################################################################################
