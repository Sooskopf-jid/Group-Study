total_revenue = 0


def rent_bike(client, station, bike_id):
    global total_revenue
    found_bike = None

    for bike in station.bikes:
        if bike.bike_id == bike_id:
            found_bike = bike
            break

    if found_bike == None:
        raise "BikeNotFound"

    station.bikes.remove(found_bike)
    client.current_bike = found_bike
    return True


def calculate_trip_cost(bike, minutes):
    cost = bike.calculate_cost(minutes)
    return cost


def return_bike(client, station, minutes):
    global total_revenue

    if client.current_bike == None:
        raise "BikeNotFound"

    bike = client.current_bike
    cost = calculate_trip_cost(bike, minutes)

    client.balance = client.balance - cost
    total_revenue = total_revenue + cost
    station.add_bike(bike)
    client.current_bike = None

    return cost


def get_total_revenue():
    global total_revenue
    return total_revenue