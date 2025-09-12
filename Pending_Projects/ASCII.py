a = input("enter character to get ASCII value ")
L = "abcdefghijklmnopqrstuvwxyz"
if a.isupper():
    print(f"ASCII value is: {L.index(a.lower())+65}")
else:
    print(f"ASCII value is: {L.index(a)+97}")


    # or

print(ord(a))