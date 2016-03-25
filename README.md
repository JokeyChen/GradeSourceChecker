# GradeSourceChecker
This is a simple script that can be scheduled to check GradeSource website update. 

## Overview
This script reads the given url webpage then find the updated time on the webpage. It then compares the time on GradeSource (time_on_gs) with the latest updated time in a local file called lastupdate. If they differ, that means GradeSource has updated the scores recently. The script then overwrites the lastupdate file with time_on_gs. Every time the script runs, it would also log the time of checking into a file called lastcheck. Both lastcheck and lastupdate are in the "ref/" directory. If there are update detected, it will then send an email to the address specified immediately. Information of email sending and url are stored in data file in "ref/" directory

## Installation
You can install this script by simply git clone the repository. Then, make sure the permission of setup.py and gs_checker.py is 744. You can check that by running command:

	ls -l *.py
If it shows "-rwxr--r--" for both files, you are good to go. Otherwise, change the mode to 744 by typing:

	chmod 744 *.py
After doing so, run the setup process by typing:

	./setup.py
And type in the information asked by the prompt. **It is your own responsibility to make sure that the information is 100% correct. Incorrect input will result in undefined behavior.**

Sender's name and receiver's name are for email message only. They would not affect the checking process. Sample output is in the *Example* section.

For Gmail users, the "smtp server" is 'smtp.gmail.com' and the port is 587. Users of other email providers can find out the corresponding server and port on the Internet.

After finishing the setup script, you can now run the gs_checker script by typing (assuming that the repository is in the home directory):

	~/GradeSourceChecker/gs_checker

If you want to run this script at specific time or day, or between certain intervals, please refer to the following section *Scheduling*.

## Example
Assume that we are now in the repository directory:

### setup.py
	$ ./setup.py
	PLEASE MAKE SURE THAT YOUR INPUT IS CORRECT!
	Now setting up...
	Please specify GradeSource url here: http://www.gradesource.com/reports/288/27682/index.html
	Please specify sender's email address here: abc.def@example.com
	Please specify email sender's name here: ABC DEF
	Please specify receiver's email address here: xyz@example.com
	Please specify email receiver's name here: XYZ
	Please specify the SMTP server here: smtp.gmail.com
	Please specify the SMTP port here: 587
	Please specify the email login (username) here: abc.def@example.com
	Please specify the email password here:
	SETUP DONE!

### gs_checker.py
	$ ./gs_checker.py
	Updated! Time is 2016-03-15 16:39:04
	$ ./gs_checker.py
	No update at 2016-03-15 16:39:24
After the first run, the receiver you specified during the setup process should receive an email about this update. 

## Scheduling
For unix system users, there is a simple solution called crontab for scheduling this script. If you want to run this script every 15 minutes, for instance, add this entry to crontab -e (assuming that this repository is in the home directory):
	
	*/15 * * * * ~/GradeSourceChecker/gs_checker.py 

Make sure you change the permission of the script first (for example, give it the permission of 744)

The script will run silently in background, even if you exit the terminal or log out of ssh. If you want to see the print message, please redirect the stdout to a file. Like this:

	*/15 * * * * ~/GradeSourceChecker/gs_checker.py &> output.txt
	
For more information of crontab, please see the man page of crontab.

	man crontab

## Improvement
I hardcoded the script to extract the time string on GradeSource because of my lack of html knowledge. Also, user's input is storing in a plain text file. This file includes user's email password unencrypted. Anyone who knows a better solution to these issues, please make a pull request. Thanks! 
