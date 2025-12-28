from car_commands import * # Andere Files importieren (baut aufeinander auf)
import time as t


greeting_text = "\n\nWillkommen im Autoverwaltungsprogramm!" \
"\nHier können sie Fahrzeuge sammeln, bearbeiten und inspizieren." \
"\nIhnen stehen noch viele weitere Funktionen zur Verfügung." \
"\nWarten sie einen Moment, bis das Programm gestartet wird."



# Begrüßung
def greeting():
    print(Fore.LIGHTBLUE_EX + greeting_text)
    print(Fore.LIGHTBLACK_EX + "\nProgramm wird gestartet", end = "")
    t.sleep(0.8)
    print(Fore.LIGHTBLACK_EX + "\rProgramm wird gestartet.", end = "")
    t.sleep(0.8)
    print(Fore.LIGHTBLACK_EX + "\rProgramm wird gestartet..", end = "")
    t.sleep(0.8)
    print(Fore.LIGHTBLACK_EX + "\rProgramm wird gestartet...", end = "")
    t.sleep(0.8)
    print(Fore.LIGHTBLACK_EX + "\rProgramm wird gestartet", end = "")
    t.sleep(0.8)
    print(Fore.LIGHTBLACK_EX + "\rProgramm wird gestartet.", end = "")
    t.sleep(0.8)
    print(Fore.LIGHTBLACK_EX + "\rProgramm wird gestartet..", end = "")
    t.sleep(0.8)
    print(Fore.LIGHTBLACK_EX + "\rProgramm wird gestartet...", end = "")
    t.sleep(2)

# Main
def main():
    greeting()
    commands()

# Mainloop
try:
    main()
except KeyboardInterrupt:
    close_program()