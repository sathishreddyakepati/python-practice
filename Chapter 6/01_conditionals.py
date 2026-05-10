#if, elif, else ladder
a = int(input("Enter your age: "))

if(a>=18):
    print("Eligible to vote!")
elif(a<=0):
    print("Invalid Age!")
else:
    print("Not eligible to vote!")

