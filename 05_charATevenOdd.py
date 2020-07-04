# print character at even number
s='satishsharma'
i=0
print("Character present at even index")
while i<len(s):
    print(s[i],end="")
    i=i+2

print()
# print character at odd number
s='satishsharma'
i=1
print("Character present at odd index")
while i<len(s):
    print(s[i],end="")
    i=i+2

print()
# second way use of slice operator
s="satishsharma"
print("character at even index ",s[0::2])
print("character at odd index ",s[1::2])