# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

# 1 apan list ko set mai include he nhi karskte hai
# 2 agr karbhi skte hote to uske value ko change nhi kar skte the kyuki set mai jo value h wo hashable honi chahiye aur list hashable nhi hoti hai.
# and you cannot even have a list as an elemnet in a set because lists are mutable and unhashable. Therefore, you cannot change the values inside a list that is contained in a set.