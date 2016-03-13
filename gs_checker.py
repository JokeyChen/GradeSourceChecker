#!/usr/bin/python
import time
import urllib
import smtplib
import os
from bs4 import BeautifulSoup

URL = 'SPECIFY GRADE SOURCE URL HERE'
SENDER = 'SPECIFY EMAIL SENDER HERE'
RECEIVERS = ['SPECIFY EMAIL RECEIVERS HERE']
MSG = """From: John Doe <johndoe@xxx.com>
To: John Doe <johndoe@yyy.com>
Subject: GradeSource Update

GradeSource Update Detected!
FEEL FREE TO MODIFY THE EMAIL MESSAGE HERE
"""
SMTP_SERVER = 'SPECIFY THE SMTP SERVER HERE. DO NOT FORGET ITS PORT BELOW'
SMTP_PORT = 587
MAIL_LOGIN = 'SPECIFY LOGIN FOR SMTP'
MAIL_PW = 'SPECIFY PASSWORD FOR SMTP HERE'


FILE_READ_MODE = 'r'
FILE_WRITE_MODE = 'w'

CHAR_NEWLINE = '\n'
TIME_STR_FORMAT = '%Y-%m-%d %H:%M:%S' # Feel free to modify the format
PARSER = 'html.parser'

# lastupdate file must be present prior to running, empty or not
LAST_UPDATE = os.path.dirname(os.path.realpath(__file__)) + '/'+ 'ref/lastupdate'
LAST_CHECK =  os.path.dirname(os.path.realpath(__file__)) + '/'+ 'ref/lastcheck'

STR_UPDATE = 'Updated! Time is'
STR_NO_UPDATE = 'No update at'
STR_ERR_SEND_EMAIL = 'Error trying to send email!'



def get_current_time_str():
    """Return the formatted current time string"""
    return time.strftime(TIME_STR_FORMAT, time.localtime())

def get_webpage():
    """Return the BeautifulSoup object from given URL and parser"""
    return BeautifulSoup(urllib.urlopen(URL).read(), PARSER)

def find_update(soup):
    """
    """
    # TODO: need to come up with a more generic way to find the update string
    update = soup.find_all('font')
    return (update[4].contents[1])[1:] + '\n'

def check_diff(time_on_gs):
    """
    """
    lastupdate = open(LAST_UPDATE, FILE_READ_MODE)
    # TODO: Error Checking
    time_stored = lastupdate.read()
    if time_stored == time_on_gs:
        return 0
    else:
        return 1
    lastupdate.close()

def update_lastupdate(time_on_gs):
    """
    """
    lastupdate = open(LAST_UPDATE, FILE_WRITE_MODE)
    # TODO: Error checking
    lastupdate.write(time_on_gs)
    lastupdate.close()

def update_lastcheck(current_time_str):
    """
    """
    lastcheck = open(LAST_CHECK, FILE_WRITE_MODE)
    # TODO: Error checking
    lastcheck.write(current_time_str + CHAR_NEWLINE)
    lastcheck.close()

def send_email():
    """
    """
    a = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    a.starttls()
    a.login(MAIL_LOGIN, MAIL_PW)
    try:
        a.sendmail(SENDER, RECEIVERS, MSG)
    except SMTPException:
        print STR_ERR_SEND_EMAIL


def main():
    current_time_str = get_current_time_str()
    soup = get_webpage()
    time_on_gs = find_update(soup)
    if check_diff(time_on_gs):
        print STR_UPDATE, current_time_str
        update_lastupdate(time_on_gs)
        send_email()
    else:
        print STR_NO_UPDATE, current_time_str
    update_lastcheck(current_time_str)


if __name__ == '__main__':
    main()