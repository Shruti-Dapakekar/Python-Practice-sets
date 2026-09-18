# A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

word = "Donkey"

with open("Practiceset 9/file.txt","r") as f:
    data = f.read()

contentNew = data.replace(word,"######")

with open("Practiceset 9/file.txt","w") as f:
    f.write(contentNew)