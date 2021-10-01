my_dict = {
    'a':50,
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 
#  expect result:-['e','b','c']
b={}
for char in my_dict:
    if char not in b:
        b[char]=1
    else:
        b[char]=b[char]+1
print(b)
