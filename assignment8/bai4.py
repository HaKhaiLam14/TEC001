import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.current_speed = max(0, min(car.max_speed, car.current_speed + speed_change))
            car.drive(1)

    def print_status(self):
        print("\n--- Race Status ---")
        print(f"{'Car':<10} {'Speed':<10} {'Distance':<15}")
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.current_speed:<10} {car.distance_traveled:<15.2f}")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False


if __name__ == "__main__":

    cars = []
    for i in range(10):
        cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0

    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            race.print_status()

    race.print_status()
    print(f"\nRace finished in {hours} hours")