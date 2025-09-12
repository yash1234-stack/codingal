#WAP to calculate electricicy bull by checking no of units consumed x<50 puc = 2.6+tax 25rs x>50 x<100 cpu 3.25+tax 35 x>100 cpu 5.26+ tax = 45, x>200 8.45 +tax75
n = int(input("enter number of units"))
amt = 0
if n>50:
    if n>100:
        if n>200:
            amt = (8.45*n)+75
        else:
            amt = (5.26*n)+45
    else:
        amt = (3.25*n)+35
else:
    amt = (2.6*n)+25

print(f"electricity bill is {amt}rs")