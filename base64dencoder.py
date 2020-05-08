#! /usr/bin/env python3

import base64
import pyperclip
import time

def print_copy_ask():
    pyperclip.copy(s2)
    print("Here's your fuckin shit: \n" + s2)
    print()
    answer = input('Would you like to do more? (y/n) \n > ')
    return answer


def bencode():
    shit = input('Enter your data to encode: \n > ')
    s2 = str(base64.b64encode(shit.encode('ascii')))
    s2 = s2[2:-1]
    return s2


def bedcode():
    shit = input('Enter your fuckin shit: \n > ')
    s2 = base64.b64decode(shit).decode('ascii')
    return s2


def beddcode():
    shit = input('Enter your fuckin shit: \n > ')
    s2 = base64.b64decode(shit).decode('ascii')
    s2 = base64.b64decode(s2).decode('ascii')
    return s2


answer = 'y'
while answer.lower() == "y":
    code = input('Would you like to encode or decode? (e/d) \n > ')
    if code.lower() == 'e':
        s2 = bencode()
        answer = print_copy_ask()
    elif code.lower() == 'd':
        s2 = bedcode()
        answer = print_copy_ask()
    elif code.lower() == 'dd':
        s2 = beddcode()
        answer = print_copy_ask()
    else:
        print('Enter the right shit dumbass 🤡 \n Try again.')
else:
    print("Goodbye")
    time.sleep(.5)