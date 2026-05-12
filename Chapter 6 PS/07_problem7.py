# 7. Write a program to find out whether a given post is talking about “Harry” or not. 
post = input("Enter post content: ")
name = "Harry"
if(name.lower() in post.lower()):
    print("Yes,post is talking about Harry")
else:
    print("NO,post is not talking about harry")