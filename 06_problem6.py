# Can you change the self-parameter inside a class to something else (say *rishabh"). Try changing self to "slf" or "rishabh" and see the effects.
from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(rishabh, fro, to):
        print(f"Ticket is booked in train no: {rishabh.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is: {randint(300, 1000)}")

t = Train(12398)
t.book("Jabalpur", "Ujjain")
t.getStatus()
t.getFare("Jabalpur", "Ujjain")

# There is no change in the output on changing the (self) to (slf) or (rishabh)