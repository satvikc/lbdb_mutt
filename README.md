#Description#
This script automatically goes through your saved emails and stores the found addresses in the lbdb database which you can use for autocompletion of your mail addresses.

##Requirements##
You should install lbdb, python 3.x  and ofcourse mutt. It will not work with python 2.x.

##Variables##

* MAILDIR : Mail directory where your mails are saved .  Change "~/Mail" to whatever you want.
* LBDB : No need to change that if you dont know what you are doing.
* FIRST_TIME : Run the script with this as 'True' first time and then it will be set to 'False'.
* DAY : If FIRST_TIME is set to false then the script will only check mails which are "DAY" days older . It is set to 1 . So you should run this script once every day. Or set it to cron to be executed daily.

##Configurations##
Open the muttrc file and set :
set query_command = "lbdbq '%s'"

##Usage##
Just run the script once and then set FIRST_TIME Variable to 'False' and set it to the cron job or manually run it daily.
When you are sending mail to someone just type few letters and press 'CTRL+t' to see the magic happen.
