# Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionErrorʼ .
try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    print(f"The Division is: {a/b}")
except ZeroDivisionError as e:
    print("Infinite")
