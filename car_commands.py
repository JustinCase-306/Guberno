from car_classes import Car, SportsCar, PickUp
from colorama import Fore, init

cars = []

init(autoreset = True)

# Befehle
def commands():
    while True:
        command_question = input("\rWelchen Befehl möchten sie ausführen? Schreiben sie /help für mehr Info. ").lower()
        if command_question == "/help":
            help_commands()
        elif command_question == "/add":
            add_vehicle()
        elif command_question == "/show":
            show_vehicle()
        elif command_question == "/delete":
            delete_vehicle()
        elif command_question == "/close":
            close_program()
        elif command_question == "/clear":
            cars.clear()
        elif command_question == "/drive":
            drive_mode()
        else:
            print("\nUngültiger Befehl!")

# Programm schließen
def close_program():
    while True:
        close = input(Fore.RED + "\n\nMöchten sie das Programm beenden? ").lower()
        if close in ["ja", "yes", "j", "y"]:
            exit()
        else:
            print("Programm wird neu gestartet.")
            return

# Fahrzeug löschen
def delete_vehicle():
    if not cars:
        print("Es gibt keine Fahrzeuge zum Löschen.")
        return
    try:
        index = int(input("\nWelche Nummer soll gelöscht werden? "))
        if 0 <= index < len(cars):
            cars.pop(index)
            print("Fahrzeug wurde gelöscht.")
        else:
            print("Ungültige Nummer.")
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")


# Fahrzeuge hinzufügen: Auto / Sportwagen / Pickup


# Fahrzeuge
def add_car():
    car = Car(
        wheels=int(input("Räder (Anzahl): ")),
        doors=int(input("Türen (Anzahl): ")),
        brand=input("Marke: "),
        model=input("Modell: "),
        year=int(input("Baujahr: ")),
        cylinders=int(input("Zylinder (Anzahl): ")),
        color=input("Farbe: "),
        ps=input("PS (Pferdestärke): "),
        speed=input("Höchstgeschwindigkeit (in km/h): ")
    )
    cars.append(car)

def add_sportscar():
    sportscar = SportsCar(
        wheels=int(input("Räder (Anzahl): ")),
        doors=int(input("Türen (Anzahl): ")),
        brand=input("Marke: "),
        model=input("Modell: "),
        year=int(input("Baujahr: ")),
        cylinders=int(input("Zylinder (Anzahl): ")),
        color=input("Farbe: "),
        ps=input("PS (Pferdestärke): "),
        speed=input("Höchstgeschwindigkeit (in km/h): "),
        wrapping=input("Folierung (falls vorhanden): "),
        exhaust=input("Auspuff/e (Anzahl): ")
    )
    cars.append(sportscar)

def add_pickup():
    pickup = PickUp(
        wheels=int(input("Räder (Anzahl): ")),
        doors=int(input("Türen (Anzahl): ")),
        brand=input("Marke: "),
        model=input("Modell: "),
        year=int(input("Baujahr: ")),
        cylinders=int(input("Zylinder (Anzahl): ")),
        color=input("Farbe: "),
        ps=input("PS (Pferdestärke): "),
        speed=input("Höchstgeschwindigkeit (in km/h): "),
        loading_area=input("Ladefläche (in Quadratmetern): ")
    )
    cars.append(pickup)

def add_vehicle():
    while True:
        vehicle_type = input("Welchen Fahrzeugtyp (Auto, Pickup, Sportwagen) möchten sie hinzufügen? ").lower()
        if vehicle_type == "auto":
            add_car()
            break
        elif vehicle_type == "pickup":
            add_pickup()
            break
        elif vehicle_type == "sportwagen":
            add_sportscar()
            break
        else:
            print("Ungültige Eingabe, bitte erneut.")

# Fahrzeuge anzeigen
def show_vehicle():
    if not cars:
        print("Keine Fahrzeuge gefunden.")
        return
    for index, car in enumerate(cars):
        print(f"\n[{index}]")
        car.overview()

# Fahrmodus
def drive_mode():
    sportscars = [car for car in cars if isinstance(car, SportsCar)]
    if not sportscars:
        print("Kein Sportwagen vorhanden.")
        return
    print("\nVerfügbare Sportwagen:")
    for index, car in enumerate(sportscars):
        print(f"[{index}] {car.brand} {car.model}")
    try:
        choice = int(input("Welchen Sportwagen willst du fahren? "))
        if 0 <= choice < len(sportscars):
            sportscars[choice].turbo()
        else:
            print("Ungültige Auswahl.")
    except ValueError:
        print("Bitte eine Zahl eingeben.")

# Hilfe
def help_commands():
    print(Fore.LIGHTGREEN_EX + "\n\nVerfügbare Befehle:"
          "\n/add fügt ein neues Fahrzeug hinzu."
          "\n/show zeigt ihre Fahrzeuge."
          "\n/delete (Fahrzeug) löscht eines ihrer Fahrzeuge."
          "\n/close beendet das Programm."
          "\n/clear löscht alle Fahrzeuge."
          "\n/drive aktiviert den Fahrmodus.\n\n\n")