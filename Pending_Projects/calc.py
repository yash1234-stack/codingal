a = int(input("enter number ")) #input for the base number
p = int(input("enter power "))  # input for exponent
result =1
for i in range(p):
    result = result*a
print(f"result ={result}")