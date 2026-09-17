# Write a python function to remove a given word from a list and strip it at the same time.

def rem(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n
    
l=["Shrutish","Shubhamsh","Harry","Himani","Akankshash","Anushkash","Komal","sh"]
print(l)
print(rem(l,"sh"))
