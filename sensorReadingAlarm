# Created by Chris Hsu
# Modified by Dan Lwo

from __future__ import print_function
import smtplib
import boto3
import json
from decimal import *

print('Loading function')

def lambda_handler(event, context):
    #get data from dynamoDB
    for record in event['Records']:
        AA = record['dynamodb']
        dName = json.dumps(AA['NewImage']['DeviceName']['S'])
        ID = json.dumps(AA['NewImage']['UUID']['S'])
        IP = json.dumps(AA['NewImage']['IP']['S'])
        TEMP = json.dumps(AA['NewImage']['Temperature']['N'])
        HUMI = json.dumps(AA['NewImage']['Humidity']['N'])
        Moment = json.dumps(AA['NewImage']['Moment']['S'])
        #set message
        text1 = dName+"\n Temperature : " +TEMP +"\n Humidity : " +HUMI
        text2 = "\n Time : " +Moment +"\n IP : " +IP    
        TEXT = text1 + text2
    
    #send mail or not
    if TEMP[1:-1] >= "28.0" or TEMP[1:-1] <= "20.0" or HUMI[1:-1] >= "60.0" or HUMI[1:-1] <= "28.0":
        gmail_user = "alert.sender@your.email.com"
        gmail_pwd = "yourEmailPassword"
        FROM = "alert.sender.name"
        #TO = event['recipient'] if type(recipient) is list else [recipient]
        TO = ["alert.receiver@your.email.com"]
        SUBJECT = "Sensor Alert from : " +dName
        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print("successfully sent the mail")
            print(dName + " Temperature : " +TEMP + " Humidity : " +HUMI +"\n Time : " +Moment)
        except:
            print("failed to send mail")
    else:
        print("Status normal. /n" + TEXT)
    
    return dName, Moment
