# FUNCTIONS WITH ARGUMENTS 

def greet(name):
    gr = "hi "+ name
    return gr
a = greet("Sunil")
print(a)

#default parameter value
def greet(name="unknown"):
    gr = "hi "+ name
    return gr
a1 = greet()
a = greet("Sunil")
print(a1)
print(a)