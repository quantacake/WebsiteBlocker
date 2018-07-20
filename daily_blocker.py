import platform
import os, os.path
import sys
import subprocess
import time
from datetime import datetime as dt


redirect = '127.0.0.1'

# add or remove websites here. 
website_list = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com']


def site_blocker():

    ops = platform.system()
    if 'darwin' in ops.lower() or 'linux' in ops.lower():
        hosts_path = '/etc/hosts'
        if os.geteuid() != 0:
            os.execvp('sudo', ['sudo', 'python3'] + sys.argv)
    else:
        print('This program cannot run unless the user is in Administrator mode. If you\'re running Windows, find the \'hosts\' file in \'C:\Windows\System32\drivers\etc\hosts\' and right click Command Prompt on the file, then click Run as Administrator and rerun this program.')
        host_path = 'C:\Windows\System32\drivers\etc\hosts'

    while True:
        # configure hours parameter to alter when a site is blocked.
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):

            print('Working hours...')
        
            with open(hosts_path, 'r+') as f:
                content = f.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        f.write(redirect + ' ' + website + '\n')

        else:
            with open(hosts_path, 'r+') as f:
                content=f.readlines()
                f.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        # if website is not in the current line, then rewrite the line. else DO NOT rewrite the line. 
                        f.write(line)
                    else:
                        print(line, 'has been deleted')
                f.truncate()
            print('Fun hours...')
        
        # loops every 5 seconds
        time.sleep(5)


site_blocker()

