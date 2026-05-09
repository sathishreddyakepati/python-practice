# Write a program to input eight numbers from the user and display all the unique 
# numbers (once).
e = set()
i=0
while(i<8):a=int(input("Enter the number: "));e.add(a);i+=1

print(e)