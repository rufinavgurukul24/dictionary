dict={"name":"raju","marks":56}
user_1=input("enetr the value which you want to check:")
i=0
while i<=len(dict):
    if user_1=="name" or user_1=="marks":
        print(user_1,"it exist")
    else:
        print(user_1,"it do not exist")
    i=i+1