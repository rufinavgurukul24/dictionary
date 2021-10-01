# output= {"M":1,"I":4,"S":4,"P":2} 
a="MISSISSIPPI"
b={}
for char in a:
    if char not in b:
        b[char]=1
    else:
        b[char]=b[char]+1
print(b)
