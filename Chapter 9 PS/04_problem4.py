# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.
word = "Donkey"
newword = "#####"
with open("file4.txt","r") as f:
    data = f.read()

data = data.replace(word,newword)

with open("file4.txt","w") as f:
    f.write(data)