# 5. Repeat program 4 for a list of such words to be censored. 

l = ["Nijam","free","diamond"]
newword = "#####"
with open("file5.txt") as f:
    content = f.read()

for word in l:
    content = content.replace(word,newword)

with open("file5.txt","w") as f:
    f.write(content)