# Write a program which finds out whether a given name is present in a list or not.

name = input("Enter your name: ")
list=["Shruti","Himani","Akanksha","Shubham","Riya","Jhon","Rohan","Anushka","Komal"]
if name in list:
    print("Your name is " + name + " present in the list.")
else:
    print("Your name is " + name + " not present in the list.")