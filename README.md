# base64-translator

## Info

Written in python.
A simple program for encoding and decoding base64 text.
No need to select the text from the terminal and copy it, the program copies the output into your clipboard.

Pyperclip will need to be installed, which can be done via pip: `pip install pyperclip`

The clean version is a vestige of previous versions containing profanity, however I will keep it up for any future interest.

## Options

In order to use this program you have to input your data and then, at the end, add an "|" followed by your options. Your options are as follows:

`-e` - encode data

`-d` - decode data

`-sn` - save under new title

`-sa` - save an append to txt doc

## Example Output
```

Enter your data:
 > This is a test encode for github | -e
Here's your data:
VGhpcyBpcyBteSB0ZXN0IGVuY29kZSBmb3IgZ2l0aHVi

Would you like to do more? (y/n) 
 > y
Enter your data:
 > QSBzdXJwcmlzZSB0byBiZSBzdXJlIGJ1dCBhIHdlbGNvbWUgb25lLg== | -d
Here's your data: 
A surprise to be sure but a welcome one.

Would you like to do more? (y/n) 
 > n
Goodbye

```
