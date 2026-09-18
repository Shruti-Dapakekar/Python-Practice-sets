#  Write a program to read the text from a given file ‘poems.txtʼ and find out whether it contains the word ‘twinkleʼ

f = open("Practiceset 9/poem.txt")
data = f.read()
if ("Twinkle" in data):
    print("The word Twinkel is present in data")
else:
    print("The word Twinkel is not present in data")

f.close()