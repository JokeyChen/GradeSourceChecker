#!/usr/bin/python
from json import dump
from os import mkdir
from getpass import getpass

STR_WELCOME_MSG = 'PLEASE MAKE SURE THAT YOUR INPUT IS CORRECT!\nNow setting up...'
STR_DONE_MSG = 'SETUP DONE!'

def print_welcome_msg():
    """Print the command line welcome message."""
    print STR_WELCOME_MSG

def generate_dict():
    """Return the data dictionary which entries are based on user input."""
    my_dict = {}
    my_dict['url'] = raw_input('Please specify GradeSource url here: ')
    sender = raw_input('Please specify sender\'s email address here: ')
    sender_name = raw_input('Please specify email sender\'s name here: ')
    receivers = raw_input('Please specify receiver\'s email address here: ')
    receivers_name = raw_input('Please specify email receiver\'s name here: ')
    my_dict['sender'] = sender
    my_dict['receivers'] = [receivers]

    my_dict['smtp_server'] = raw_input('Please specify the SMTP server here: ')
    try:
        my_dict['smtp_port'] = int(raw_input('Please specify the SMTP port here: '))
    except ValueError:
        my_dict['smtp_port'] = int(raw_input('Invalid port. Please try again: '))

    my_dict['mail_login'] = raw_input('Please specify the email login (username) here: ')
    my_dict['mail_pw'] = getpass('Please specify the email password here: ')

    my_dict['msg'] = """From: %s <%s>
To: %s <%s>
Subject: GradeSource Update

GradeSource Update Detected!
""" % (sender_name, sender, receivers_name, receivers)

    return my_dict

def create_dir():
    """Make the reference director if not exists."""
    try:
        mkdir('ref')
    except OSError:
        # ref directory already exists
        pass

def create_data(my_dict):
    """Create the data file."""
    f = open('ref/data', 'w')
    dump(my_dict, f)
    f.close()

def create_lastupdate():
    """Create the lastupdate file."""
    f = open('ref/lastupdate', 'w')
    f.close()

def print_done_msg():
    """Print the command line done message."""
    print STR_DONE_MSG

def main():
    print_welcome_msg()
    my_dict = generate_dict()
    create_dir()
    create_data(my_dict)
    create_lastupdate()
    print_done_msg()

if __name__ == '__main__':
    main()
