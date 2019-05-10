import os
import sys

import pandas as pd 
import Numpy as np
import datetime 
from openpyxl import Workbook
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def send_email(subject,content,receiver):
	
	sender='1476006@qq.com'
	subject=subject
	smtpserver='email.address'
	user='myname'
	password='helloworld'
	msg = MIMEMultipart()
        myroot = os.path.dirname(os.path.abspath(__file__))
        att = MIMEText(open(myroot + '/' + string, 'rb').read(),'base64','gb2312')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment;filename= %s' % string.encode("utf-8")
        msg.attach(att)
       msg['Subject'] = Header(subject, 'utf-8')
       msg['From'] = username
       msg['TO'] = ','.join(receiver_list)
       smtp = smtplib.SMTP_SSL()
       smtp.connect(smtpserver)
       smtp.login(username, password)
       smtp.sendmail(sender, receiver_list, msg.as_string())
       smtp.quit()
def get_tomorrow():
	tomorrow=str(datetime.now()+timedelta(day))
	weekday=datetime.today().weekday()
	begin=datetime.now().date-timedelta(day=1000000)
	end=datetime.now().date-timedelta(day=20000)
	period_number=(end-begin).days
	
	







if __name_=='__main__':
	string='send email to my address'
	subject='hello'
	receiver=['1126006@qq.com']
	send_email(subject,string,receiver)
	
	
	print(1234556)


