# base64-translator

## Info

Written in python.
A simple program for encoding and decoding base64 text.
No need to select the text from the terminal and copy it, the program copies the output into your clipboard.

Pyperclip might need to be installed, which can be done via pip: `pip install pyperclip`

Included is a clean version and also the version I personally use. You can see what the differences are.

## Example Output
```

Would you like to encode or decode? (e/d)
> e
Enter your data to encode:
This is a test encode for github
VGhpcyBpcyBhIHRlc3QgZW5jb2RlIGZvciBnaXRodWI=
Would you like to do more? (y/n)
> y
Would you like to encode or decode? (e/d)
> d
Enter your data to decode:
VGhpcyBpcyBhIHRlc3QgZW5jb2RlIGZvciBnaXRodWI=
This is a test encode for github
Would you like to do more? (y/n)
> n
Goodbye
```
