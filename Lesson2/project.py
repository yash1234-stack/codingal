#raj's friends
yash = '30/03/2008'
Aditi = '02/06/2008'
poonam = '10/10/2008'
virat = '19/9/2008'
jai = '29/02/2008'
print(yash+" "+Aditi+" "+poonam+ " "+virat+" "+jai+" "+"\n")
'''
can be printed through a simple print stattement as shown above but that through that you will not get the corresponding names
therefore the bottom code can be used
''' 
i=0
#taking two arrays instead so that we can print the names and birthdays together
name = ["yash","aditi", "poonam", "virat", "jai"]
date = ['30/03/2008','02/06/2008','10/10/2008','19/9/2008', '29/02/2008']
for i in range(len(name)):
    print(name[i], end="\t"); print(date[i])
