from main import *
from os import path



park = Park("veluwe")
huis1 = Bungalow(200, 4, byWater=True, theme="Mario")
huis2 = TentArea(10)
huis3 = HotelRoom()
huis3 = HotelRoom()

piet = Customer("Piet")
park.add(huis1)
park.add(huis2)

def test_reservation():
    reservation = Reservation(park, piet, "TentArea", 3)
    result = reservation.submit()
    assert result == True

def test_reserveBungalow():
    reservation = Reservation(park, piet, "Bungalow", 4, options={"byWater":True, "theme":"Mario"})
    result = reservation.submit()
    assert result == True

def test_Hoteltoomanypeople():
    reservation = Reservation(park, piet, "HotelRoom", 3)
    result = reservation.submit()
    assert result == False

def test_doubleReservation():
    reservation = Reservation(park, piet, "TentArea", 2)
    result = reservation.submit()
    assert result == False

def test_reservation_export():
    reservation = Reservation(park, piet, "HotelRoom", 1)
    reservation.submit()
    reservation.export()
    assert path.exists("veluwe_Reservation4.txt")


# def test_split(self):
#     s = 'hello world'
#     self.assertEqual(s.split(), ['hello', 'world'])
#     # check that s.split fails when the separator is not a string
#     with self.assertRaises(TypeError):
#         s.split(2)

if __name__ == "__main__":
    test_reservation()
    test_reserveBungalow()
    test_Hoteltoomanypeople()
    test_doubleReservation()
    test_reservation_export()
    print("Everything passed")





# reservation1 = Reservation(park, piet, 4,options={"theme":"Mario","byWater":True})
# reservation1.submit()
# reservation1.export()

# print(piet)