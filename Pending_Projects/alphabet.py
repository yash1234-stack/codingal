a = input("enter character to check if it is an alphabet or not")

if (ord(a)<=90 and ord(a)>=60) or (ord(a)>=97 and ord(a)<=122): #checking for aschii values since checking every single alohabet would be too much
    print("the character is an alphabet")
else: 
    print("it is not an alphabet")
    