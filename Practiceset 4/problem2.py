#WAP to accept marks of 6 students and display them in a sprted manner
marks=[]
for i in range(6):
    mark=int(input("Enter the marks of student {}:".format(i+1)))
    marks.append(mark)
print("The Sorted marks all 6 students are:",sorted(marks))
