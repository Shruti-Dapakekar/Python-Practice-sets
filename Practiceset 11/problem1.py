#  Create a class (2-D vector) and use it to create another class representing a 3-D vector
class twod:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class threed(twod):
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


t1 = twod(3,5)
t1.show()
t2 = threed(5,3,2)
t2.show()