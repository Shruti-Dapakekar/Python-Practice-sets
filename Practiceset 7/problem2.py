# Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul","Shruti"]
for i in l:
    if i.startswith("S"):
        print(f"Hello {i}")
