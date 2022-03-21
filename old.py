per1=int(input("enter age of person1:"))
per2=int(input("enter age of person2:"))
per3=int(input("enter age of person3:"))
if per1>per2 and per1>per3:
    print("person1 is oldest")
elif per2>per1 and per2>per3:
    print("person2 is oldest")
else:
    print("person3 is oldest")
if per1<per2 and per1<per3:
    print("person1 is youngest")
elif per2<per1 and per2<per3:
    print("person2 is youngest")
else:
    print("person3 is youngest")