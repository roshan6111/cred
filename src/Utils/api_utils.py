from datetime import datetime
# from Service import 
from flask import Flask, current_app
from Service import PersonalExtractorFactory
import base64, os
from os import path
import json
from PdfAnalyser import PdfAnalysers


def remove_file_from_input(verificationInput):
    if "file" in verificationInput:
        del verificationInput['file']


def get_verification(verificationInput):
    """
    verification API main function
    :param matching_details: json input with xpressId, taskId, 
    :return: response and run thread on background
    """
    user_details_app = Flask(__name__)
    user_details_app.config.from_object('config.BaseConfig')
    response = {
        'errorCode': 100,
        '_id': '',
        'xpressId': '',
        'taskId': '',
        'error': ''
    }
    if response['errorCode'] == 100:
        try:
                # creating file code
                filebase64 = ''
                if "file" in verificationInput:
                        filebase64 = verificationInput['file']
                        pdfName = ''
                        if "fileName" in verificationInput:
                                if verificationInput["fileName"].replace(" ",""):
                                        pdfName = verificationInput['fileName'].replace(" ","")
                                else:
                                        pdfName = random.getrandbits(16)
                        else:
                                pdfName = random.getrandbits(16)
                        
                filePath = 'static/DownloadPdf/' + pdfName
                # write pdf file
                with open(os.path.expanduser(filePath), 'wb') as fout:
                        fout.write(base64.decodestring(filebase64))
                # end of creatin file code
                
        except:
                response['error'] = 'file not stored properly'
                return response        
        remove_file_from_input(verificationInput)
        try:         
                file = current_app.config.get('LOCAL_FILE_PATH') + verificationInput["fileName"]
                if path.exists(file) and file.lower().endswith('.pdf'):
                        if verificationInput["bankName"] in PersonalExtractorFactory.EXTRACTOR_MAP_1:
                                extractor_counter = 1
                                if verificationInput["bankName"] in PersonalExtractorFactory.EXTRACTOR_TYPE_MAP:
                                        extractor_counter = PersonalExtractorFactory.EXTRACTOR_TYPE_MAP[verificationInput["bankName"]]
                                counter = 1
                                while counter <= extractor_counter:
                                        EXTRACTOR_MAP = 'EXTRACTOR_MAP_'+ str(counter)
                                        extractor = getattr(PersonalExtractorFactory, EXTRACTOR_MAP)[verificationInput["bankName"]]
                                        result = extractor.extract(file,verificationInput["password"])
                                        if 'transactions' in result:
                                                if len(result['transactions']) > 0:
                                                        analyserData = PdfAnalyser.analyser(result, verificationInput["bankName"])
                                                        return json.dumps(result)
                                                        break
                                                else:
                                                        counter += 1
                                        return result

                return "roshan"
        except Exception as e:
                print (e)
                return "error"


