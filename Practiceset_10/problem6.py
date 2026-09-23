# Can you change the self-parameter inside a class to something else (say “harry”)? Try changing self to “slf” or “harry” and see the effects.
from random import randint
import random
# Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways
class Train:
    def __init__(slf,trainno):
        slf.trainno = trainno
        
    def book(shru,destination,source):
        print(f"Tickets is booked in train no: {shru.trainno} from {source} to {destination}")
    def getStatus(slf):
        print(f"Train no: {slf.trainno} is running on time")
    def getFare(slf,destination,source):
        print(f"Tickets is booked in train no: {slf.trainno} from {source} to {destination} is {random.randint(222,5555)}")

t = Train(12345)
t.book("Chhatrapati Sambhajinagar","Delhi")
t.getStatus()
t.getFare("Chhatrapati Sambhajinagar","Delhi")