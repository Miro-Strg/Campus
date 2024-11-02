import random
import time

def generiere_zahlen():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def starte_spiel():
    num1, num2 = generiere_zahlen()
    print(f"Was ist {num1} + {num2}?")
    correct_answer = num1 + num2

    start_time = time.time()
    user_answer = input("Deine Antwort: ")
    end_time = time.time()
    gemessene_zeit = end_time - start_time

    if int(user_answer) == correct_answer:
        print("Richtig!")
    else:
        print(f"Falsch! Die korrekte Antwort ist {correct_answer}")

    print(f"Du hast {gemessene_zeit:.2f} Sekunden gebraucht, um deine Antwort einzugeben.")

# Starte das Spiel
starte_spiel()