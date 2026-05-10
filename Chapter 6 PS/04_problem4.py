#  Write a program to find whether a given username contains less than 10 
# characters or not. 

username = input("Enter username: ")
if(len(username)<10):
    print(username,": Contains less than 10 Characters")
else:
    print(username,": Contains more than or equal 10 Characters")

