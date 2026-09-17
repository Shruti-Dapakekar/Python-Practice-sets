# Write a python function to print first n lines of the following pattern.
# ***
# **        n =3
# *

def star(n):
    if n == 0:
        return
    print("*"*n)
    star(n-1)   # (n-1) esliye kiya coz upr se niche ate time ek-ek star kaam hora hai thats why
star(5)