# GradeSourceChecker
This is a simple script that can be schedule to run to check GradeSource website update. 

## Overview
This script reads the given url webpage then find the updated time on the webpage. It then compares the time on GradeSource (time_on_gs) with the latest updated time in a local file called lastupdate. If they differ, that means GradeSource has updated the scores recently. The script then overwrites the lastupdate file with time_on_gs. Every time the script runs, it would also log the time of checking into a file called lastcheck. Both lastcheck and lastupdate are in the "ref/" directory. If there are update detected, it will then send an email to the address specified immediately. 

## Installation
You can install this script by simply git clone the repository. Then, open the gs_checker.py file, modify all the constants filled with CAPITAL LETTERS (from URL all the way down to MAIL_PW).

For RECEIVERS, one can specify many receivers all at once. Please make sure that the list contains at least one item.

For Gmail users, the SMTP_SERVER is 'smtp.gmail.com' and the port is 587. Users of other email providers can find out the corresponding server and port on the Internet.

Make sure that the lastupdate file is present! Or the IOError will occur. The lastupdate file can be either an empty file or real file that contains the time string. As long as the file is present, you are good to go.

If you want to run this script at specific time or day, or between certain intervals, please refer to the following section **Scheduling**.

## Scheduling
For unix system users, there is a simple solution called crontab for scheduling this script. If you want to run this script every 15 minutes, for instance, add this entry to crontab -e (assuming that this repository is in the home directory):
	
	*/15 * * * * ~/GradeSourceChecker/gs_checker.py 

Make sure you change the permission of the script first (for example, give it the permission of 744)

The script will run silently in background, even if you exit the terminal or log out of ssh. If you want to see the print message, please redirect the stdout to a file. Like this:

	*/15 * * * * ~/GradeSourceChecker/gs_checker.py &> output.txt
	
For more information of crontab, please see the man page of crontab.

	man crontab

## Improvement
I hardcoded the script to extract the time string on GradeSource because of my lack of html knowledge. Anyone who knows a better solution to get the time string, please make a pull request. Thanks! 
