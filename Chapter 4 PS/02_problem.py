# Write a program to accept marks of 6 students and display them in a sorted 
# manner. 

marks = []
i = 0

while(i<6): a = int(input("Enter marks: ")); marks.insert(i,a);i+=1

marks.sort()

print(marks)