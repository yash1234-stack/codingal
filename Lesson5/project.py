temp = input("enter temperature")
temp = temp.upper()
if temp == "COLD": 
    print("not suitable for light clothes")
if temp == "WARM" or temp == "HOT": 
    print("suitable for light clothes")

temp = int(input("enter temp in C"))

if temp<25:
    print("not suitable for light clothes")
else:
    print("you can wear light clothes")
