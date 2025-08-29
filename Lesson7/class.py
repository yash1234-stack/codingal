a = [1, 2, 3]
b = [1, 2, 3]

if a is b: 
    print("same")
else:
    print("not same")
#not same since it checks both adress and value

if a==b:
    print("same")
else:
    print("not same")
#same since it only checks value

if 2 in a: 
    print("yes")
else:
    print("no") 
    
a=5 