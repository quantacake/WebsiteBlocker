Python Mega Course • Project 3

This project was created from 'The Python Mega Course: Build 10 Real World Applications' by Ardit Sulce. https://www.udemy.com/the-python-mega-course/learn/v4/overview



This productivity program allows you to block websites depending on time of day. 

Steps:
1. Add websites you want to block in the website_list variable. 
2. On line 28, change the hour of day to block your website_list during those hours.
3. Saving and running the file will prompt Unix based operating systems to input their password to enter sudo. This will allow the program to read and append information into your 'hosts' file. If you are using Windows operating system, you will need to have Administrator access for the file which can be found C:\Windows\System32\drivers\etc\hosts. 

If you want the program to run on reboot/restart, you will need to:
1. Open a crontab with sudo: sudo crontab -e
2. In the file add: @include python3 path/to/file/website_blocker.py


