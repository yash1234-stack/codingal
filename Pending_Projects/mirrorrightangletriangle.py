a = int(input())
k=a
for i in range(a):
    for j in range(k):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
    k=k-1