import time
import base64
import pyperclip

answer = 'y'
while answer.lower() == "y":
    user_data = input('Enter your data:\n > ')
    code = input('Would you like to encode or decode? (e/d) \n > ')
    if code.lower() == 'e':
        s2 = str(base64.b64encode(user_data.encode('ascii')))
        s2 = s2[2:-1]
    elif code.lower() == 'd':
        s2 = base64.b64decode(user_data).decode('ascii')
    elif code.lower() == 'dd':
        s2 = base64.b64decode(user_data).decode('ascii')
        s2 = base64.b64decode(s2).decode('ascii')
    else:
        print('Please correctly choose one of the options. \n Try again. \n 🤡')
    pyperclip.copy(s2)
    print("Here's your data: \n" + s2)
    answer = input('Would you like to do more? (y/n) \n > ')
else:
    print("Goodbye")
    time.sleep(.5)
