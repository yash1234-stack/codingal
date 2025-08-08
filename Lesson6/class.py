# a = [10, 12, 0]
# c=0
# for i in range(len(a)):
#     if(bool(a[i])==False):
#         c=1
#         break
#     else:
#         continue
# if c==1:
#     print("everything is not True")
# else:
#     print("everything is true")




# a=12
# b=10
# c=0
# if a and b and c: 
#     print("all true")
# else:
#     print("not all true")




a = True
b = not a 
c = "yash"
d = not c
print(b)
print(d)
e = 123
f = not e
print(f)


#weight in kg / (height in cm * height in cm)) * 10,000

weight = float(input("enter your weight in kg"))
height = float(input("enter ur height in cm"))

BMI = weight/(height/100)**2
print(f"your BMI is {BMI} and you are ", end="")
if BMI < 18.4:
    print("underweight")
elif BMI >18.4 and BMI < 24.9:
    print("healthy")
elif BMI >24.9 and BMI < 29.9:
    print("overweight")
elif BMI >29.9 and BMI < 34.9:
    print("severly overweight")
else:
    print("obese")