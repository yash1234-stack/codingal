# n=int(input("enter number "))
# if n>50:
#     if n>100:
#         print("number is greater than 100")
#     else:
#         print("less than 100 greater than 50")

# else:
#     print("number is smaller than 50")

    #activity 

#WAP to check if they can skip exam medical cause/attendence>75%

med = input("Do you have a medical condition? ")
if med == 'n':
    a = int(input("what is your attendence? "))
    if a>=75:
        print("you are allowed to give the exam")
    else:
        print("you are not allowed to give the exam")
elif med == 'y':
    print("you are not allowed to give the exam")
else:
    print("invalid")



