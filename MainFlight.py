import random
import re
class travel:

    
    def __init__(self, source, destination, distance, time, privilege):
        self.source = source
        self.destination = destination
        self.distance = distance
        self.time = time
        self.privilege = privilege
        self.cost = 0


    def travel_fare(self):
        if self.privilege == "FIRST CLASS":
            self.cost = self.distance * 150
        elif self.privilege == "ECONOMY":
            self.cost = self.distance * 20
        return self.cost


#t1 = travel("New York", "Beijing", 8000, 10, "ECONOMY")
#t2 = travel("London", "New York", 6000, 6, "FIRST CLASS")
#t3 = travel("Bengaluru", "Abu Dhabi", 3000, 3, "BUSINESS CLASS")
    

class PNR:

    def __init__(self, PNR_no, ticket):
        self.PNR_no = PNR_no
        self.ticket = ticket
    
    def __str__(self):
        return f"PNR NO --> [{self.PNR_no}] Travelling From {self.ticket.source} To {self.ticket.destination}"

#p1 = PNR("24613", t1)
#print(p1)


destinations = {"New York":1, "London":2, "Beijing":3, "Tokyo":4, "Bengaluru":5, "Abu Dhabi":6}
distance_time = {12:(5600, 5), 21:(5600, 5), 23:(8200,10), 32:(8200,10), 34:(2100, 3), 43:(2100, 3), 45:(6650,10), 54:(6650,10), 56:(2750,4), 65:(2750,4), 13:(11000,14), 31:(11000,14), 14:(10900, 14), 41:(10900, 14), 15:(13360, 17), 51:(13360, 17), 16:(11040, 14), 61:(11040, 14), 24:(8200,11), 42:(8200,11), 25:(9570,9), 52:(9570,9), 26:(5500,7), 62:(5500, 7), 31: (10980, 13), 13:(10980, 13), 35:(5575, 10), 53:(5575, 10), 36:(6000, 9), 63:(6000, 9), 46:(8200,13), 64:(8200,13), 41:(10850, 13), 14:(10850,13), 42:(6000,13), 24:(6000,13), 43:(6700,11), 34:(6700,11), 51:(13400,12), 15:(13400, 12), 52:(8000,11), 25:(8000,11), 53:(7650,10), 35:(7650,10), 54:(8500,11), 45:(8500,11), 61:(11040,15), 16:(11040,15), 62:(5520, 8), 26:(5520,8), 63:(6000, 7), 36:(6000, 7), 64:(8100, 9), 46:(8100, 9)}

#Please update the distance and time data for calculations purposes.

all_pnr = []
all_details = []

def booking():
    """To book Ticket"""


    src = input("FROM: ")
    dest = input("TO: ")
    dist = distance_time[int(str(destinations[src]) + str(destinations[dest]))][0]
    ti = distance_time[int(str(destinations[src]) + str(destinations[dest]))][1]
    pri = input("FIRST CLASS OR ECONOMY: ")
    
    t1 = travel(src, dest, dist, ti, pri)
    p1 = PNR(random.randrange(1, 1000000), t1)
    print(f"Booking Confirmed with Total Amount {p1.ticket.travel_fare()} press YES OR NO To Confirm")
    if input("") == "YES":
        print(f"TICKET CONFIRMED for {p1}")
        #all_details.append(p1)   #Ticket will be saved in a global list.
        with open('bookingdetails.txt', 'a') as b:
            b.write(f"{p1}")
            b.write("\n")

    else:
        print(f"BOOKING CANCELLED")

def check_pnr(val):
    """To check the details of the booked Ticket"""


    with open('bookingdetails.txt', 'r') as f:
        all_tickets = f.readlines()
        for ticket in all_tickets:
            for pnr in ticket:
                all_pnr.append(pnr)
        
    if val in all_pnr:

        
        for p1 in all_details:
            print(p1)
            if int(p1.PNR_no) == int(val):
                print("TICKET FOUND")
                print(f"--------------------------------------\n| {p1.ticket.source}      >>>>>>>      {p1.ticket.destination}  |\n\n| DISTANCE                     {p1.ticket.distance} |\n\n| TIME:                     {p1.ticket.time} HRS |\n--------------------------------------")
                break
    else:
        print("INCORRECT PNR NO OR TICKET NOT CONFIRMED")

if __name__ == "__main__":
    while True:
        print("1.TICKET BOOKING OR 2.CHECK PNR STATUS AND -1 TO EXIT")
        n = int(input("ENTER OPTION: "))
        if n == 1:
            booking()
        elif n == 2:
            check_pnr(input("ENTER PNR NO "))
        elif n == -1:
            break
