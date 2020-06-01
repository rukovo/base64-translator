# base64-translator

## Info

Written in python.
A simple program for encoding and decoding base64 text.
No need to select the text from the terminal and copy it, the program copies the output into your clipboard.

Pyperclip will need to be installed, which can be done via pip: `pip install pyperclip`

The app.py program will give you more options, including saving your decodes/encodes to a text document. The app-old.py is an older version of the program that uses simple yes/no level questions for options and does not include the ability to save your data to a file. This one will just decode/encode and then will copy it to your clipboard. With the old version there is a hidden option to type `dd` when it asks if you want to encode or decode. This will decode the inputted data twice, which I thought would be a nice feature to include since I encounter double-encoded strings somewhat frequently.

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
