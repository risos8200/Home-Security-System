from sms_sender import sendSMS
import json
with open("creds.json") as f:
    creds = json.loads(f.read())
from_number = creds["from_number"]
way2sms_password = creds["way2sms_pass"]
to_number = creds["to_number"]
def send_sms(message_str):
    message_list = [sendSMS(message_str[i:i+140], from_number, way2sms_password, to_number)
                    for i in range(0,len(message_str),140)]
