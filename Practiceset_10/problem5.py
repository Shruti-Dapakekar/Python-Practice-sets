from random import randint
import random
# Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways
class Train:
    def __init__(self,trainno):
        self.trainno = trainno
        
    def book(self,destination,source):
        print(f"Tickets is booked in train no: {self.trainno} from {source} to {destination}")
    def getStatus(self):
        print(f"Train no: {self.trainno} is running on time")
    def getFare(self,destination,source):
        print(f"Tickets is booked in train no: {self.trainno} from {source} to {destination} is {random.randint(222,5555)}")

t = Train(12345)
t.book("Chhatrapati Sambhajinagar","Delhi")
t.getStatus()
t.getFare("Chhatrapati Sambhajinagar","Delhi")