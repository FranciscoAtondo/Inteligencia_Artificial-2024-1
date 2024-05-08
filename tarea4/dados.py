from abc import ABC, abstractmethod
import random

class Dados(ABC):
    def __init__(self):
        self.dinero = 0

    def jugar(self):
        action = input("Elija si desea quedarse(1) o salir(2): ")
        if action == '1':
            dice_roll = random.randint(1, 6)
            print("El dado lanzó:", dice_roll)
            if dice_roll <= 2:
                print("El juego ha terminado. Tiene $", self.dinero, ".")
                return False
            else:
                self.dinero += 4
                print("Tiene ahora $", self.dinero)
                return True
        elif action == '2':
            self.dinero += 10
            print("El juego ha terminado. Usted ganó $10 y tiene en total $", self.dinero)
            return False
        else:
            print("Entrada no válida. Intente de nuevo.")
            return self.jugar()

    def play(self):
        round_number = 1
        while True:
            print("\nRonda", round_number)
            if not self.jugar():
                break
            round_number += 1
