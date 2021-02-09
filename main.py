# todo: convert collections to sets from lists

class Park():
    def __init__(self):
        self.day = 0
        self.places = []

    def add(self, place):
        self.places.append(place)

class Customer():
    id_counter = 0

    def __init__(self, name):
        self.id = Customer.id_counter
        Customer.id_counter += 1
        self.name = name
        self.reservations = []

    def __repr__(self):
        return "{}{} {} \nreservations:\t{}".format(self.__class__.__name__, str(self.id), self.name, (self.reservations))


class Reservation():
    id_counter = 0

    def __init__(self, park, customer, people):
        self.id = Reservation.id_counter
        Reservation.id_counter += 1
        
        self.park = park
        self.customer = customer
        self.people = people
        self.customer.reservations.append(self)
        self.status = "PENDING"
        self.places = []

    def submit(self):
        for place in self.park.places:
            
            if place.reserve(self):
                self.places.append(place)
                self.status = "APPROVED"
                print("reserved place{} for Customer{} {}".format(place.id, self.customer.id, self.customer.name))
                return True
        self.status = "REJECTED"
        print("can't make reservation in place{} for Customer{} {}".format(place.id, self.customer.id, self.customer.name))
        return False


    def __repr__(self):
        return "{}{} ({} people in {}) {}".format(self.__class__.__name__, self.id,  self.people, self.places, self.status)


class Place():
    id_counter = 0

    def __init__(self, area, capacity):
        self.id = Place.id_counter
        Place.id_counter += 1

        self.area = area
        self.capacity = capacity
        self.occupied = False

    def reserve(self, reservation):
        self.reservation = reservation

        if not self.occupied and reservation.people <= self.capacity:
            self.occupied = True
            return True
        else:
            return False


    def __repr__(self):
        return "{}{} {}".format(self.__class__.__name__, self.id, "OCCUPIED" if self.occupied else "VACANT")


class TentArea(Place):
    def __init__(self, area):
        if area >= 9:
            super().__init__(area, capacity = float("inf"))
        else:
            raise Exception("tentarea should be 9m^2 or more")

        self.cost = 4*area


class Bungalow(Place):
    def __init__(self, area = 100, capacity = 4, byWater=False, theme=None):
        if capacity in (2,4,7):
            if theme and capacity != 4:
                raise Exception("Bungalows with a theme should have a capacity of 4")
            super().__init__(area, capacity)
        else:
            raise Exception("capacity of Bungalow should be 2, 4 or 7")

        self.byWater = byWater
        self.theme = theme

        if self.theme
            self.cost = 110
        elif capacity == 2:
            self.cost = 50
        elif capacity == 4:
            self.cost = 80
        elif capacity == 7:
            self.cost = 140
    

class HotelRoom(Place):
    def __init__(self, area = 50, capacity = 2, bedtype = "single", amenities = []):
        if capacity in (1,2):
            super().__init__(area, capacity)
        else:
            raise Exception("capacity of HotelRoom should be 1 or 2")

        self.bedtype = bedtype
        self.amenities = amenities
        self.cost = 60 #Todo cost based number of people in reservation

park = Park()
huis1 = Bungalow(200, 2)
huis2 = TentArea(10)

park.add(huis1)
park.add(huis2)

piet = Customer("Piet")
reservation1 = Reservation(park, piet, 4)
reservation1.submit()

print(piet)












