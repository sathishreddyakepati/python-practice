# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 
letter = '''  Dear <|Name|>,\n \tYou are selected!\n \t<|Date|> ''' 
l = letter.replace("<|Name|>","sathish").replace("<|Date|>","13 September 2006")
print(l)