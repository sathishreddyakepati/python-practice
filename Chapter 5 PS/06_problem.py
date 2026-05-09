# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 
dict ={}
i = 0
while(i<4):a =input("Enter your name: ");b=input("Enter your fav language: ");dict.update({a:b});i+=1
print(dict.items()) 