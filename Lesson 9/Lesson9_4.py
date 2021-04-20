class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} started")

    def stop(self):
        print(f"Car {self.name} stopped")

    def turn(self, direction):
        print(f"Car {self.name} turned {direction}")

    def show_speed(self):
        print(f"Car {self.name} speed is {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Car {self.name} is speeding over limit")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Car {self.name} is speeding over limit")
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


town_car = TownCar(70, "black", "MB", False)
sport_car = SportCar(180, "red", "Enzo", False)
work_car = WorkCar(30, "white", "Audi", False)
police_car = PoliceCar(90, "black", "Ford", True)

town_car.go()
town_car.show_speed()
town_car.stop()

sport_car.go()
sport_car.show_speed()
sport_car.turn("right")
sport_car.stop()
