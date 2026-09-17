# Write a python program using function to convert Celsius to Fahrenheit.
def c_to_f():
    f = ( c *(9/5) + 32)
    print(f"{f}")
    
c = int(input("Enter Temperature in Celsius: "))
c_to_f()