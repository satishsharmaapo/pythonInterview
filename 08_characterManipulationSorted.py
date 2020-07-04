# Q write a program for the following requirement?
# input : a3z2b4
# output: aaabbbbzz(sorted String)
s=input("Enter Some String where alphabet symbol should be followed by digits: ")
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
print(''.join(sorted(output)))
