
def prime(a):
    k=0#counter
    for i in range(2, int(a**(1/2))+1, 1):
        if a%i == 0:
            k+=1
            break
        else:
            continue
    if k>0:
        return False
    else:
        return True

def listprime(a):
    b = []
    for i in range(1, a+1):
        if prime(i):
            b.append(i)
        else:
            continue 
    return b

a = int(input("enter number to check the prime numbers till that number "))
print(listprime(a))