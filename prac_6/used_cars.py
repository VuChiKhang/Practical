from prac_6.car import Car

def main():
    # my_car = Car (180)
    # my_car.drive(30)
    limo=Car(100, "My Limousine")
    limo.add_fuel(20)

    print("fuel = ", limo.fuel)
    limo.drive(115)
    print("odo = ", limo.odometer)
    print(limo)

    print("Car {}, {}".format(limo.fuel, limo.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo))

main()


