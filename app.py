import os
import time
import base64
import pyperclip

abspath = os.path.dirname(os.path.abspath(__file__))
os.chdir(abspath)

answer = 'y'
while answer.lower() == 'y':
    user_input = input("Enter you're data\n > ")
    user_input = user_input.split('|')
    user_data = user_input[0].strip()
    user_args = user_input[1].replace(' ', '')
    user_args = user_args.split('-')
    if 'e' in user_args:
        s2 = str(base64.b64encode(user_data.encode('ascii')))
        s2 = s2[2:-1]
    if 'd' in user_args:
        s2 = base64.b64decode(user_data).decode('ascii')
    if 'sn' in user_args:
        list = open('link_list.txt', 'a')
        title = input('What would you like the title to be?\n > ')
        title = title.title()
        title = title.center(50, '-')
        list.append('\n' + title + '\n' + s2 + '\n')
    if 'sa' in user_args:
        list = open('list.txt', 'a')
        list.append(s2 + '\n')
    print(s2)
    pyperclip.copy(s2)
    answer = input('Would you like to do more?\n > ')
else:
    print('Goodbye')
    time.sleep(.5)
