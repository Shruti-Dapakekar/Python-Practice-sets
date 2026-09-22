# Write a program to find out whether a file is identical and matches the content of another file.
with open("Practiceset 9/this.txt") as f:
    content1=f.read()
with open("Practiceset 9/copy_this.txt") as f:
    content2=f.read()
if (content1==content2):
    print("Yes the files are identical")
else:
    print("No the files are not identical")