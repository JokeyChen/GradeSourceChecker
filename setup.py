#!/usr/bin/python
from json import dump

MY_DICT = {'url': 'SPECIFY GRADE SOURCE URL HERE',
'sender': 'SPECIFY EMAIL SENDER HERE',
'receivers': ['SPECIFY EMAIL RECEIVERS HERE'],
'smtp_server': 'SPECIFY THE SMTP SERVER HERE. DO NOT FORGET ITS PORT BELOW',
'smtp_port': 587,
'mail_login': 'SPECIFY LOGIN FOR SMTP',
'mail_pw': 'SPECIFY PASSWORD FOR SMTP HERE',
'msg': """From: John Doe <johndoe@xxx.com>
To: John Doe <johndoe@yyy.com>
Subject: GradeSource Update

GradeSource Update Detected!
FEEL FREE TO MODIFY THE EMAIL MESSAGE HERE
"""
}

def create_data():
    f = open('ref/data', 'w')
    dump(MY_DICT, f)
    f.close()

def create_lastupdate():
    f = open('ref/lastupdate', 'w')
    f.close()

def main():
    create_data()
    create_lastupdate()

if __name__ == '__main__':
    main()

