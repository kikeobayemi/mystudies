
# creating 2 variables for the rot13 algorithm technique. the contents in x is replaced with the contents in y
x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
y = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
# reading content of text file
with open('c:/Users/KIKE/Desktop/pythonprojects/plaintext.txt') as f:
    contents = f.read()
    print(contents) #print to screen from text file

ciphertxt = contents.maketrans(x, y) #maketrans function maps the characters in y to x

#write to second text file
with open('c:/Users/KIKE/Desktop/pythonprojects/plaintext2.txt', 'w') as g:
    contents2 = contents.translate(ciphertxt)
    g.write(contents2) #translate plaintext using the mapping specifies by maketrans
    print(contents2) #print the contents of second text file to screen


