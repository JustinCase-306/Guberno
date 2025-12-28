import time as t
from colorama import Fore, init # Colorama

init(autoreset = True)

# Auto
class Car:
    def __init__(self, wheels, doors, brand, model, year, cylinders, color, ps, speed):
        self.wheels = wheels
        self.doors = doors
        self.brand = brand
        self.model = model
        self.year = year
        self.cylinders = cylinders
        self.color = color
        self.ps = ps
        self.speed = speed

    def overview(self):
        print(Fore.BLUE + f"\n\nDies sind die Eckdaten zu deinem Auto:\n"
              f"- Modell: {self.model}\n"
              f"- Marke: {self.brand}\n"
              f"- Baujahr: {self.year}\n"
              f"- Türen: {self.doors}\n"
              f"- Zylinder: {self.cylinders}\n"
              f"- Räder: {self.wheels}\n"
              f"- Farbe: {self.color}\n"
              f"- PS: {self.ps}\n"
              f"- Höchstgeschwindigkeit: {self.speed}\n")

# Sportwagen
class SportsCar(Car):
    def __init__(self, wheels, doors, brand, model, year, cylinders, color, ps, speed, wrapping, exhaust):
        super().__init__(wheels, doors, brand, model, year, cylinders, color, ps, speed)
        self.wrapping = wrapping
        self.exhaust = exhaust

    @staticmethod
    def turbo(self):
        print("WRUMMMMM!")
        t.sleep(0.8)
        print("WRUMMMM!")
        t.sleep(1)
        print("WRUMM!")
        t.sleep(1)
        print("WRUMMMMMMM!")
        t.sleep(1)
        print("WRUMMM!")
        t.sleep(1)
        print("WRUMMMMM!")
        t.sleep(1)
        print("WRUMM!")
        t.sleep(1)
        print("WRUMMMMMMMM!")
        t.sleep(1)
        print("WRUMMMMM!")
        t.sleep(1)
        print("WRUMM!")
        t.sleep(1)
        print("WRUMMMM!")
        t.sleep(2)
        print("Turbo beendet!")

    def overview(self):
        print(Fore.BLUE + f"\n\nDies sind die Eckdaten zu deinem Sportwagen:\n"
              f"- Modell: {self.model}\n"
              f"- Marke: {self.brand}\n"
              f"- Baujahr: {self.year}\n"
              f"- Türen: {self.doors}\n"
              f"- Zylinder: {self.cylinders}\n"
              f"- Räder: {self.wheels}\n"
              f"- Folierung: {self.wrapping}\n"
              f"- Auspuff/e: {self.exhaust}\n"
              f"- Farbe: {self.color}\n"
              f"- PS: {self.ps}\n"
              f"- Geschwindigkeit: {self.speed}\n")

# Pickup
class PickUp(Car):
    def __init__(self, wheels, doors, brand, model, year, cylinders, color, ps, speed, loading_area):
        super().__init__(wheels, doors, brand, model, year, cylinders, color, ps, speed)
        self.loading_area = loading_area

    def overview(self):
        print(Fore.BLUE + f"\n\nDies sind die Eckdaten zu deinem Pickup:\n"
              f"- Modell: {self.model}\n"
              f"- Marke: {self.brand}\n"
              f"- Baujahr: {self.year}\n"
              f"- Türen: {self.doors}\n"
              f"- Zylinder: {self.cylinders}\n"
              f"- Räder: {self.wheels}\n"
              f"- Ladefläche (in Quadratmetern): {self.loading_area}\n"
              f"- Farbe: {self.color}\n"
              f"- PS: {self.ps}\n"
              f"- Geschwindigkeit: {self.speed}\n")