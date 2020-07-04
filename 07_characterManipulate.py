# Q Write a program for the following requirement ?
# INPUT WILL be in form of as A2B3C1
# OUTPUT WILL BE AABBBC
s=input("Enter Some String where alphabet symbol should be followed by digits: ")
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
print(output)
