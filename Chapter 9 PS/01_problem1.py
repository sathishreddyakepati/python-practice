# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 


with open("poems.txt") as f:
    text = f.read().lower()
    if("twinkle" in text):
        print("File contains twinkle")
    else:
        print("File does not contain twinkle")
    

    
    
