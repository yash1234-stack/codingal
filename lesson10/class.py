# #pattern reverse 1234
n = int(input("enter number of rows "))
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print("")

for i in range(n, 0,-1):
    for j in range(0, n-i):
       print(" ", end="")
    for k in range(0, 2*i-1):
        print("*", end="")
    print("")
