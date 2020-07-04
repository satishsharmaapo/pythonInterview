#  reverse string 
# Slice operator means a peace      abcdefdhijk  

s="satish"
print(s[::-1])    

#hsitas
# s[begin:end:step]     end -1 then reverse  (right to left)
# step will never be zero otherwise it will show error.
# step will be 1 then it will show all the value.
# s  a  t  i  s  h 
#  0  1  2  3  4  5
# -6  -5 -4 -3 -2  -1

# second method :
s="satish"
r=reversed(s)
for i in r:
    print(i,end="")
print()

# third with use the ''.join() function to 

r=reversed("priyanka")
output=''.join(r)
print(output)

# fourth using while loop
st="mango"
i=len(st)-1
output1=''
while i>=0:
    output1 = output1 + st[i]
    i=i-1 
print(output1)