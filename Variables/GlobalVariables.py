# Global variables are those created outside a function. But they can be used both inside and outside functions
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# To be used inside a function, the global keyword has to be used on the variable.
y = "Nice"

def yfunc():
    global y
    y = "Formidable"
    print("Le Seigneur est formidable")

yfunc()