import unittest
# todo: convert collections to sets from lists

class Park():
    def __init__(self, name):
        self.day = 0
        self.name = name
        self.places = []

    def add(self, place):
        self.places.append(place)

    def __repr__(self):
        return self.name


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

    def __init__(self, park, customer, kind, people, options = None):
        self.id = Reservation.id_counter
        Reservation.id_counter += 1
        
        self.park = park
        self.customer = customer
        self.kind = kind
        self.people = people
        self.options = options
        self.customer.reservations.append(self)
        self.status = "PENDING"
        self.places = []

    def submit(self):
        for place in self.park.places:
            if self.kind == place.__class__.__name__:
                if place.reserve(self):

                    self.places.append(place)
                    self.status = "APPROVED"
                    print("reserved place{} for Customer{} {} {}".format(place.id, self.customer.id, self.customer.name, self.kind))
                    return True
        self.status = "REJECTED"
        print("can't make reservation in place{} for Customer{} {} {}".format(place.id, self.customer.id, self.customer.name, self.kind))
        return False

    def export(self):
        print(f"export{self.id}")
        f = open(f"{self.park}_{self.__class__.__name__}{self.id}.txt", "w")
        f.write(f"Park: {self.park}\n")
        f.write(f"Reservation: {self.__class__.__name__}{self.id}\n")
        f.write(f"Customer: {self.customer.name}\n")
        f.write("\n")
        f.write(f"people: {self.people}\n")
        f.write(f"places: {self.places}\n")
        f.write(f"options: {self.options}\n")
        f.write(f"reservation status: {self.status}\n")
        f.close()
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
            super().__init__(area = 20, capacity = 4)
        else:
            raise Exception("tentarea should be 9m^2 or more")

        self.cost = 4*area

    def reserve(self, reservation):
        return super().reserve(reservation)



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

        if self.theme:
            self.cost = 110
        elif capacity == 2:
            self.cost = 50
        elif capacity == 4:
            self.cost = 80
        elif capacity == 7:
            self.cost = 140

    def reserve(self, reservation):
        if not super().reserve(reservation):
            return False

        if not reservation.options:
            return True
        for option, value in reservation.options.items():
            if option == "byWater":
                if value == True and not self.byWater:
                    self.occupied = False
                    return False

            if option == "theme":
                if value != self.theme:
                    self.occupied = False
                    return False
        return True
    

class HotelRoom(Place):
    def __init__(self, area = 50, capacity = 2, bedType = "double", amenities = []):
        if capacity in (1,2):
            if capacity == 1 and bedType == "double":
                raise Exception("can't have a double bed in a room for one")
            super().__init__(area, capacity)
        else:
            raise Exception("capacity of HotelRoom should be 1 or 2")

        self.bedType = bedType
        self.amenities = amenities
        self.cost = 60 #Todo cost based number of people in reservation

    def reserve():
        if not super().reserve(reservation):
            return False

        if not reservation.options:
            return True

        for option, value in reservation.options.items():
            if option == "bedType":
                if value != self.bedType:
                    self.occupied = False
                    return False
        return True


           
# park = Park("veluwe")
# huis1 = Bungalow(200, 4, byWater=True, theme="Mario")
# # huis2 = TentArea(10)

# park.add(huis1)
# # park.add(huis2)

# piet = Customer("Piet")
# reservation1 = Reservation(park, piet, "HotelRoom", 4,options={"theme":"Mario","byWater":True})
# reservation1.submit()
# reservation1.export()

# print(piet)












