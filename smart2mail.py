#!/usr/bin/python
import os
from time import sleep

import smtplib

def send_email(host, subject, to_addr, from_addr, body_text, login, passwd):

    BODY = u"\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject ,
        "",
        body_text
    )).encode('utf-8')

    mail = smtplib.SMTP(host, 587)
    mail.ehlo()
    mail.starttls()
    mail.login(login,passwd)
    mail.sendmail(from_addr,[to_addr],BODY)
    mail.close()



if __name__ == "__main__":
    host = "smtp.smtp.ru"
    subject = "SMART data from Host"
    to_addr = "reciever@mail.ru"
    from_addr = "host@mail.ru"
    login = "username@mail.ru"
    passwd = "yourPassHere"
    hdd_list=['sda','sdb']
    body_text=""
    body_text += os.popen("cat /proc/mdstat").read()
    for hdd in hdd_list:
        body_text +=  os.popen("smartctl -a /dev/"+hdd).read()
    send_email(host, subject, to_addr, from_addr, body_text, login, passwd)
