#!/usr/bin/python
from json import dump
from os import mkdir

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

def create_dir():
    """Make the reference director if not exists."""
    try:
        mkdir('ref')
    except OSError:
        # ref directory already exists
        pass

def create_data():
    """Create the data file."""
    f = open('ref/data', 'w')
    dump(MY_DICT, f)
    f.close()

def create_lastupdate():
    """Create the lastupdate file."""
    f = open('ref/lastupdate', 'w')
    f.close()

def main():
    create_dir()
    create_data()
    create_lastupdate()

if __name__ == '__main__':
    main()

