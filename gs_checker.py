#!/usr/bin/python
import time
import urllib
import smtplib
import os
from bs4 import BeautifulSoup
from json import load

FILE_READ_MODE = 'r'
FILE_WRITE_MODE = 'w'

CHAR_NEWLINE = '\n'
TIME_STR_FORMAT = '%Y-%m-%d %H:%M:%S' # Feel free to modify the format
PARSER = 'html.parser'

# lastupdate and data file must be present prior to running, empty or not
LAST_UPDATE = os.path.dirname(os.path.realpath(__file__)) + '/'+ 'ref/lastupdate'
LAST_CHECK =  os.path.dirname(os.path.realpath(__file__)) + '/'+ 'ref/lastcheck'
DATA = os.path.dirname(os.path.realpath(__file__)) + '/'+ 'ref/data'

STR_UPDATE = 'Updated! Time is'
STR_NO_UPDATE = 'No update at'
STR_ERR_SEND_EMAIL = 'Error trying to send email!'

def read_data():
    """
    """
    # TODO: Error Checking
    return load(open(DATA, FILE_READ_MODE))

def get_current_time_str():
    """Return the formatted current time string."""
    return time.strftime(TIME_STR_FORMAT, time.localtime())

def get_webpage(my_data):
    """Return the BeautifulSoup object from given URL and parser."""
    return BeautifulSoup(urllib.urlopen(my_data['url']).read(), PARSER)

def find_update(soup):
    """Return the Last Update time found from the given soup object.

    Keyword arguments:
    soup -- the GradeSource soup object
    """
    # TODO: need to come up with a more generic way to find the update string
    update = soup.find_all('font')
    return (update[4].contents[1])[1:] + '\n'

def check_diff(time_on_gs):
    """Return 0 if there are no difference between time on GradeSource and
    locally stored time, and return 1 if there are difference.

    Keyword arguments:
    time_on_gs -- string extracted from the GradeSource webpage
    """
    lastupdate = open(LAST_UPDATE, FILE_READ_MODE)
    # TODO: Error Checking
    time_stored = lastupdate.read()
    if time_stored == time_on_gs:
        return 0
    else:
        return 1
    lastupdate.close()

def update_lastupdate(time_string):
    """Overwrite the lastupdate file with given time string.

    Keyword arguments:
    time_string -- formatted time string to be written
    """
    lastupdate = open(LAST_UPDATE, FILE_WRITE_MODE)
    # TODO: Error checking
    lastupdate.write(time_string)
    lastupdate.close()

def update_lastcheck(time_string):
    """Overwrite the lastcheck file with given time string.

    Keyword arguments:
    time_string -- formatted time string to be written
    """
    lastcheck = open(LAST_CHECK, FILE_WRITE_MODE)
    # TODO: Error checking
    lastcheck.write(time_string + CHAR_NEWLINE)
    lastcheck.close()

def send_email(my_data):
    """Send email with provided information."""
    a = smtplib.SMTP(my_data['smtp_server'], my_data['smtp_port'])
    a.starttls()
    a.login(my_data['mail_login'], my_data['mail_pw'])
    try:
        a.sendmail(my_data['sender'], my_data['receivers'], my_data['msg'])
    except SMTPException:
        print STR_ERR_SEND_EMAIL


def main():
    my_data = read_data()
    current_time_str = get_current_time_str()
    soup = get_webpage(my_data)
    time_on_gs = find_update(soup)
    if check_diff(time_on_gs):
        print STR_UPDATE, current_time_str
        update_lastupdate(time_on_gs)
        send_email(my_data)
    else:
        print STR_NO_UPDATE, current_time_str
    update_lastcheck(current_time_str)


if __name__ == '__main__':
    main()
