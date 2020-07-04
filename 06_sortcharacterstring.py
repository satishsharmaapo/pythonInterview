# Q Assume input string contains nly alphabet symbols and digits . write a program to sort characters of the string
# ,first alphabet symbols followed by digits?

# INPUT: B4A1D3
# OUTPUT: ABD134
s="B4A1D3"
print(sorted(s)) # in list form ['1', '3', '4', 'A', 'B', 'D']
alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
print(alphabets)
print(digits)
print(''.join(sorted(alphabets)+sorted(digits)))