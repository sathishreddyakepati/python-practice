# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.
#we can also use -> k1 in text...
text = input("Enter the text: ")

k1 = "Make a lot of money"
k2 = "buy now"
k3 = "subscribe this"
k4 = "click this"
n1 = text.count(k1)+text.count(k2)+text.count(k3)+text.count(k4)

if(n1>0):
    print("Message is Spam!")

else:
    print("Message is not Spam!")



