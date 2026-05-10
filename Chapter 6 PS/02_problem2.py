# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
math = int(input("Enter maths marks: "))
phy = int(input("Enter physics marks: "))
che = int(input("Enter chemistry marks: "))
if(math<33 or phy<33 or che<33):print("Failed!,sub perct should be atleast 33")
if((math+phy+che)/3 <40):print("Failed-Total less than 40 perct")
else:print("Passed!")