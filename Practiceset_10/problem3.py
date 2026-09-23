# Create a class with a class attribute a; create an object from it and set ‘aʼ directly using ‘object.a = 0ʼ. Does this change the class attribute?
class Programmer():
    a = "Python"#class attribute

o = Programmer()
print(o.a)#prints class attribute because instance attribute is not present
o.a=0#Instance attrin=bute is set
print(o.a)#prints the instance attribute because instance attribut is present
print(Programmer.a)#prints the class attribute