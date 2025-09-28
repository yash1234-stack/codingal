a  = int(input("Enter number"))
# for i in range(a+1):
#     for j in range(0, i):
#         print("*", end="")
#     print()
k=0
for i in range(a+1):
    for j in range(0, i):
        print(k+1, end=" ")
        k=k+1
    print()
