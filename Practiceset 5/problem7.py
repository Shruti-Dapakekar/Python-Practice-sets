# If the names of 2 friends are same; what will happen to the program in problem 6?
dict ={}
a1= input("Enter your name:")
b1= input("Enter your favorite language:")
dict.update({a1:b1})
a2= input("Enter your name:")
b2= input("Enter your favorite language:")
dict.update({a2:b2})
a3= input("Enter your name:")
b3= input("Enter your favorite language:")
dict.update({a3:b3})
a4= input("Enter your name:")
b4= input("Enter your favorite language:")
dict.update({a4:b4})
print(dict)
# If the names of 2 friends are same; then the value of the first friend will be replaced by the value of the second friend. 
# The dictionary will contain only one entry for that name with the latest value.
#but if the name is unique or the value is unique then the dictionary will contain all the entries as they are unique.