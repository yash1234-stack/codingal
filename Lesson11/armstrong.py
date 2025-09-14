a = int(input("enter number to check if it is an armstrong number"))
copy = a
sum =0
while a!=0:
    sum+=(a%10)**3
    a //=10
 
print(sum)
if sum == copy:
    print("the number is an armstrong number")
else:
    print("the number is not an armstrong number")

    