import base64
import pyperclip
import time

def print_copy_ask():
    print(s2)
    pyperclip.copy(s2)
    print("Would you like to do more? (y/n)")
    answer = input('> ')
    return answer


answer = 'y'
while answer.lower() == "y":
    print('Would you like to encode or decode? (e/d)')
    code = input('> ')
    if code.lower() == 'e':
        print('Enter your data to encode:')
        shit = input()
        s2 = str(base64.b64encode(shit.encode('ascii')))
        s2 = s2[2:-1]
        answer = print_copy_ask()
    else:
        print('Enter your fuckin shit')
        shit = input()
        s2 = base64.b64decode(shit).decode('ascii')
        answer = print_copy_ask()
else:
    print("Goodbye")
    time.sleep(.5)