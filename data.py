#python has the following in-built data types namely 
#Text type : str
#Numerical types : int, float, complex
#Sequence types : list,tuple,range
#mapping type : dict
#Set types : set, frozenset
#boolean type : bool
#binary types : bytes, bytearray, memoryview
#none type : NoneType

# to know the data type of any value assigned to a variable,
# we use the type() function


x = "Hello World!"
print(x)
print(type(x))

SellingPrice = 5000
print(SellingPrice)
print(type(SellingPrice))

y = 20.44
print(y)
print(type(y))

m = 1j
print(m)
print(type(m))

fruits = ["apples","strawberry","kiwi"]
print(fruits)
print(type(fruits))

colours = ("Yellow","Red","Orange")
print(colours)
print(type(colours))


ang = range(6)
print(ang)
print(type(ang))

tin = {"name":"John","age":36}
print(tin)
print(type(tin))

tin2 ={"apple","banana","cherry"}
print(tin2)
print(type(x))

tin3 = frozenset({"apple","banana"})
print(tin3)
print(type(tin3))

s = True
print(s)
print(type(s))


p = b"Hello"
print(p)
print(type(p))

q = bytearray(5)
print(q)
print(type(q))

r = memoryview(bytes(5))
print(r)
print(type(r))

t = None
print(t)
print(type(t))