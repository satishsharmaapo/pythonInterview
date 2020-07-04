input="learning python is very easy"
# output: easy very is python learning
out=''
out=input.split()
print(out)
# ['learning', 'python', 'is', 'very', 'easy']
print(out[::-1])
# ['easy', 'very', 'is', 'python', 'learning']
# here order of list is reversed by [::-1] slicing in list is applicable.
# use join

output=' '.join(out[::-1])
print(output)
# easy very is python learning