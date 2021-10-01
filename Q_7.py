from typing import ValuesView


dict=[
     {"first":"1"}, 
     {"second":"2"},
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
k=[]
for i in dict:
    for x in i.values():
        if x not in k:
            k.append(x)
print(k)