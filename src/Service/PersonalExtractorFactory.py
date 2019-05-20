from PersonalExtractors.AllahabadBankExtractor import allahabad_bank_extractor
from PersonalExtractors.AndhraBankExtractor import andhra_bank_extractor, andhra_bank_extractor_2
from PersonalExtractors.AxisBankExtractor import axis_bank_extractor
from PersonalExtractors.BandhanBankExtractor import bandhan_bank_extractor, bandhan_bank_extractor_2
from PersonalExtractors.BankOfBarodaBankExtractor import bank_of_baroda_bank_extractor, \
    bank_of_baroda_bank_extractor_2
from PersonalExtractors.BankOfIndiaExtractor import bank_of_india_bank_extractor, bank_of_india_bank_extractor_2
from PersonalExtractors.BankOfMaharashtraExtractor import bank_of_maharashtra_extractor
from PersonalExtractors.CanaraBankExtractor import canara_bank_extractor
from PersonalExtractors.CentralBankOfIndiaBankExtractor import central_bank_of_india_bank_extractor
from PersonalExtractors.CitiBankExtractor import citi_bank_extractor
from PersonalExtractors.CitiUnionBankExtractor import citi_union_bank_extractor
from PersonalExtractors.CorporationBankExtractor import corporation_bank_extractor
from PersonalExtractors.DenaBankExtractor import dena_bank_extractor
from PersonalExtractors.DigiBankExtractor import digi_bank_extractor
from PersonalExtractors.FederalBankExtractor import federal_bank_extractor, federal_bank_extractor_2
from PersonalExtractors.HdfcBankExtractor import hdfc_bank_extractor, hdfc_bank_extractor_2
from PersonalExtractors.ICICIBankExtractor import icici_bank_extractor, icici_bank_extractor_2
from PersonalExtractors.IDBIBankExtractor import idbi_bank_extractor
from PersonalExtractors.IndianBankExtractor import indian_bank_extractor
from PersonalExtractors.IndianOverseasBankExtractor import indian_overseas_bank_extractor
from PersonalExtractors.InduslandBankExtractor import indusland_bank_extractor
from PersonalExtractors.JKBankExtractor import jk_bank_extractor
from PersonalExtractors.KarnatakaBankExtractor import karnataka_bank_extractor
from PersonalExtractors.KarurVysyaBankExtractor import karur_vysya_bank_extractor
from PersonalExtractors.KotakBankExtractor import kotak_bank_extractor, kotak_bank_extractor_2
from PersonalExtractors.PnbBankExtractor import pnb_bank_extractor
from PersonalExtractors.RblBankExtractor import rbl_bank_extractor
from PersonalExtractors.SouthIndianBankExtractor import south_indian_bank_extractor
from PersonalExtractors.StandardCharteredBankExtractor import standard_chartered_bank_extractor
from PersonalExtractors.StateBankOfIndiaExtractor import state_bank_of_india_extractor
from PersonalExtractors.SyndicateBankExtractor import syndicate_bank_extractor
from PersonalExtractors.UnionBankExtractor import union_bank_extractor
from PersonalExtractors.UnitedBankExtractor import united_bank_extractor
from PersonalExtractors.YesBankExtractor import yes_bank_extractor

EXTRACTOR_MAP_1 = {
    'ANDHRA BANK': andhra_bank_extractor,
    'AXIS BANK': axis_bank_extractor,
    'BANDHAN BANK LIMITED': bandhan_bank_extractor,
    'BANK OF BARODA': bank_of_baroda_bank_extractor,
    'BANK OF INDIA': bank_of_india_bank_extractor,
    'BANK OF MAHARASHTRA': bank_of_maharashtra_extractor,
    'CANARA BANK': canara_bank_extractor,
    'CENTRAL BANK OF INDIA': central_bank_of_india_bank_extractor,
    'CITI BANK': citi_bank_extractor,
    'CITI UNION BANK LIMITED': citi_union_bank_extractor,
    'CORPORATION BANK': corporation_bank_extractor,
    'DENA BANK': dena_bank_extractor,
    'DIGI_BANK': digi_bank_extractor,
    'FEDERAL BANK': federal_bank_extractor,
    'HDFC BANK': hdfc_bank_extractor,
    'ICICI BANK': icici_bank_extractor,
    'IDBI BANK': idbi_bank_extractor,
    'INDIAN BANK': indian_bank_extractor,
    'INDIAN OVERSEAS BANK': indian_overseas_bank_extractor,
    'INDUSLAND BANK': indusland_bank_extractor,
    'JK_BANK': jk_bank_extractor,
    'KARNATAKA BANK LIMITED': karnataka_bank_extractor,
    'KARUR VYSYA BANK': karur_vysya_bank_extractor,
    'KOTAK MAHINDRA BANK LIMITED': kotak_bank_extractor,
    'PUNJAB NATIONAL BANK': pnb_bank_extractor,
    'RBL BANK Limited': rbl_bank_extractor,
    'SOUTH INDIAN BANK': south_indian_bank_extractor,
    'STANDARD CHARTERED BANK': standard_chartered_bank_extractor,
    'STATE BANK OF INDIA': state_bank_of_india_extractor,
    'SYNDICATE BANK': syndicate_bank_extractor,
    'UNION BANK OF INDIA': union_bank_extractor,
    'UNITED BANK OF INDIA': united_bank_extractor,
    'YES BANK': yes_bank_extractor,
    'ALLAHABAD BANK': allahabad_bank_extractor,
}

EXTRACTOR_TYPE_MAP = {
    'HDFC BANK': 2,
    'ANDHRA BANK': 2,
    'FEDERAL BANK': 2,
    'ICICI BANK': 2,
    'BANK OF BARODA': 2,
    'KOTAK MAHINDRA BANK LIMITED': 2,
    'BANK OF INDIA': 2,
    'BANDHAN BANK LIMITED': 2,
}

EXTRACTOR_MAP_2 = {
    'HDFC BANK': hdfc_bank_extractor_2,
    'ANDHRA BANK': andhra_bank_extractor_2,
    'FEDERAL BANK': federal_bank_extractor_2,
    'ICICI BANK': icici_bank_extractor_2,
    'BANK OF BARODA': bank_of_baroda_bank_extractor_2,
    'KOTAK MAHINDRA BANK LIMITED': kotak_bank_extractor_2,
    'BANK OF INDIA': bank_of_india_bank_extractor_2,
    'BANDHAN BANK LIMITED': bandhan_bank_extractor_2,
}
