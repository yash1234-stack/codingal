import matplotlib.pyplot as plt 
import numpy as np 

student_names = ["raj", "yash", "sam", "jai"]
student_marks = [50, 40, 32, 28]

marksperc = []
for i in range(4):
    marksperc.append((student_marks[i]/50)*100)

print(marksperc)
plt. title("student marks")
plt.ylabel("Marks")
plt.xlabel("names")
# plt.plot(student_names, marksperc, marker = 'o', ms = 5, mec = 'r') #x axis, y axis
plt.plot(student_names, marksperc, linestyle = 'dashed', linewidth =1) 
plt.show()

