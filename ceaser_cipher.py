#!/usr/bin/env python3

import time

print("======================================")
print("         CEASER CIPHER TOOL")
print("======================================")

a=input("Enter text to encrypt your data: ")
s=" "
if s in a:
    a=a.replace(s , "")

y=a.upper()
a4=len(a)
print("1.Encrypt")
print("2.Decrypt")
a2=int(input("Choose any 2 options: "))
a3=int(input("Shifting number: "))
print("Encrypting...")
time.sleep(2)

loop=0

if a2 == 1:
    for i in range(a4):
        c=ord(y[loop])
        d=((c - 65 + a3) % 26 +65)
        print(chr(d).lower(), end="")
        loop=loop+1

if a2 == 2:
    for j in range(a4):
        c=ord(y[loop])
        d=((c - 65 +a3) % 26 +65)
        print(chr(d).lower(), end="")
        loop=loop+1
    



