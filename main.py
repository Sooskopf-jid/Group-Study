from bike_class import Bike, Station
from client_class import Client
from part3_ride import *

stationA = Station("A")
stationB = Station("B")

stations = [stationA, stationB]

bike1 = Bike(1001, "regular")
bike2 = Bike(1002, "electric")
bike3 = Bike(1003, "regular")
bike4 = Bike(1004, "electric")
bike5 = Bike(1005, "regular")

stationA.add_bike(bike1)
stationA.add_bike(bike2)
stationA.add_bike(bike5)

stationB.add_bike(bike4)
stationB.add_bike(bike3)

Vasya = Client("Vasya", 420)
Mykola = Client("Mykola", 2500)

def admin_report():
    print(f"======Звіт Адміністратора======")
    print(f"Заробіток мережі: {get_total_revenue()}")
    for station in stations:
        print(f"Велосипедів на {station.name}: {len(station.bikes)}")

def main():

    while True:
        try:
            rent_bike(Vasya,stationA,1001)
        except:
            print("Візьміть інший велосипед")
            break #test
        else:
            calculate_trip_cost(bike1, 30)
            return_bike(Vasya,stationB,30)
            break

    while True:
        try:
            rent_bike(Mykola, stationA, 1002)
        except:
            print("Візьміть інший велосипед")
            break
        else:
            calculate_trip_cost(bike2, 30)
            return_bike(Mykola, stationB, 30)
            break

    while True:
        try:
            rent_bike(Vasya, stationA, 1004)
        except:
            print("Візьміть інший велосипед")
            break
        else:
            calculate_trip_cost(bike4, 30)
            return_bike(Vasya, stationB, 30)
            break


main()
admin_report()