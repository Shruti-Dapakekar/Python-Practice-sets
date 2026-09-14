
# Write a program to find out whether a given post is talking about “Shruti” or not.
post = input("Enter the post: ")

if "Shruti".lower() in post.lower():
    print("Yes, the post is talking about Shruti.")
else:
    print("No, the post is not talking about Shruti.")