# Write a program to find the sum of first n natural numbers using while loop.
a = int(input("Enter a number:"))
i = 1
sum = 0
while (i<=a):
    sum += i
    i+=1

print(sum)

# using for loop
# for i in range(1,a+1):
#     sum += i
# print(sum)