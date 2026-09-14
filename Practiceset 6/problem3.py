# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

l = input("Enter the text: ")

if (( p1 in l) or (p2 in l) or (p3 in l) or (p4 in l)):
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
