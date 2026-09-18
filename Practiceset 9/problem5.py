# Repeat program 4 for a list of such words to be censored.
words = ["Donkey","sad","ganda","good"]

with open("Practiceset 9/file.txt","r") as f:
    data = f.read()
    
for word in words:
    data = data.replace(word,"#" * len(word))

with open("Practiceset 9/file.txt","w") as f:
    f.write(data)