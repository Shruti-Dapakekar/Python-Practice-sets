# Write a program to mine a log file and find out whether it contains ‘pythonʼ.
with open("Practiceset 9/log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Python is present")
else:
    print("Python is not present")