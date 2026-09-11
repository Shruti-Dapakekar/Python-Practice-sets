# If languages of two friends are same; what will happen to the program in problem 6?
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
#if the languages of 2 friends are same; then the value can be same for different keys (names) in the dictionary. The dictionary will contain all the entries as they are unique by their keys (names).

#but if the name is unique or the language is unique then the dictionary will contain all the entries as they are unique.