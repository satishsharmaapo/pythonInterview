#Q write a program to reverse every second word in input string
input = "One two three four five six"
     #   0   1   2     3    4    5
     # odd index reverse
l=input.split()  #['One', 'two', 'three', 'four', 'five', 'six']
print(l)
i=0
l1=[]
while i<len(l):
    if(i%2==0):
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
print(l1)  #['One', 'owt', 'three', 'ruof', 'five', 'xis']
print(' '.join(l1)) # One owt three ruof five xis