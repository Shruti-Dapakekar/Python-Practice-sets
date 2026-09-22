# Write a python program to rename a file to “renamed_by_python.txt”.
with open("Practiceset 9/old.txt") as f:
    content = f.read()
with open("Practiceset 9/renamed_by_python.txt","w") as f:
    f.write(content)