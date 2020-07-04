input=input("Enter your statement : ")
# Output: hsitaS reawtfoS noituloS
l=input.split()
print(l)
# ['Satish', 'Software', 'Solution']

l1=[]
for word in l:
    l1.append(word[::-1])
print(l1)

# ['hsitaS', 'erawtfoS', 'noituloS']
output=' '.join(l1)
print(output)
# hsitaS erawtfoS noituloS