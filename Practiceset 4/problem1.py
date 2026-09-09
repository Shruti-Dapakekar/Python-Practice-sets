#program to list 7 fruits in a list entered by the user

fruits = []
for i in range(7):
    fruit = input("Enter the name of fruit {}: ".format(i + 1))
    fruits.append(fruit)

print("The list of fruits is:", fruits)