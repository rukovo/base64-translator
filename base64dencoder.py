#! /usr/bin/env python3

import base64
import pyperclip
import time
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
link_list = 'link_list.txt'
arguments = {'decode': '-d',
             'encode': '-e', 'save new': '-sn',
             'save append': '-sa',
             'decode twice': '-dd'}


def list_title(width):
    link_title = input('What do you want the title to be?\n > ')
    link_title = link_title.title()
    title_title = link_title.center(width, '-')
    return title_title


answer = 'y'
while answer.lower() == "y":
    user_input = input('Enter your data')
    user_list = user_input.split('|')
    user_data = user_list[0].strip()
    user_args = user_list[1].replace(' ', '')
    user_args = user_args.split('-')
    if 'e' in user_args:
        s2 = str(base64.b64encode(user_data.encode('ascii')))
        s2 = s2[2:-1]
    if 'd' in user_args:
        s2 = base64.b64decode(user_data).decode('ascii')
    if 'sn' in user_args:
        open_list = open(link_list, 'a')
        title_title = list_title(40)
        open_list.write('\n' + title_title + '\n' + s2 + '\n')
        open_list.close()
    if 'sa' in user_args:
        open_list = open(link_list, 'a')
        open_list.write(s2 + '\n')
        open_list.close()
    pyperclip.copy(s2)
    print(f"\n Here's your data:\n{s2}\n")
    answer = input('Would you like to do more? (y/n) \n > ')
else:
    print("Goodbye")
    time.sleep(.5)
