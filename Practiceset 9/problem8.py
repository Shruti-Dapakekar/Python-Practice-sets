# Write a program to make a copy of a text file “this.txt”.
with open("Practiceset 9/this.txt") as f:
    content = f.read()
with open("Practiceset 9/copy_this.txt","w") as f:
    f.write(content)
