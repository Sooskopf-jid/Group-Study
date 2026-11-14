class Bike:
    RATES = {
        "regular": 2,
        "electric": 5,
    }

    def __init__(self, bike_id: int, bike_type: str):
        if bike_type not in self.RATES:
            raise ValueError(f"Невідомий тип велосипеда: {bike_type}")
        self.bike_id = bike_id
        self.bike_type = bike_type
        self.rate_per_minute = self.RATES[bike_type]

    def calculate_cost(self, minutes: int) -> int:
        if minutes < 0:
            return 0
        return minutes * self.rate_per_minute


class Station:
    def __init__(self, name: str):
        self.name = name
        self.bikes: list[Bike] = []

    def add_bike(self, bike: Bike) -> None:
        self.bikes.append(bike)

    def take_bike(self, bike_type: str | None = None) -> Bike | None:
        for index, bike in enumerate(self.bikes):
            if bike_type is None or bike.bike_type == bike_type:
                return self.bikes.pop(index)
        return None

    def count_bikes(self) -> int:
        return len(self.bikes)