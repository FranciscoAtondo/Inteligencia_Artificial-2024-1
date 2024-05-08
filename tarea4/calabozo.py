import time
from abc import ABC
from IPython.display import clear_output

class Calabozo(ABC):
    def __init__(self):
        self.mapa = [[0]*4 for _ in range(4)]

    def initial_state(self) -> list:
        self.mapa[0][3] = 1
        self.mapa[1][3] = -1
        self.mapa[3][0] = "p"
        return self.mapa

    def block_state(self) -> list:
      self.mapa[0][3] = 1
      self.mapa[1][2] = None
      self.mapa[3][0] = "p"
      return self.mapa

    def lava_state(self) -> list:
      self.mapa[0][3] = 1
      self.mapa[2][2] = -50
      self.mapa[2][3] = -50
      self.mapa[3][0] = "p"
      return self.mapa

    def jugar(self):
        x = 3
        y = 0
        while True:
            try:
                for i in range(4):
                    print(self.mapa[i])
                action = int(input("Elija la dirección a moverse: Derecha(1), Izquierda(2), Abajo(3), Arriba(4): "))
                # Derecha
                if action == 1:
                    if y+1 >= len(self.mapa) or self.mapa[x][y+1] == None:
                        clear_output(wait=True)
                        print("Accion invalida, hay un muro ahi.")
                        continue
                    if self.mapa[x][y+1] == 0:
                        self.mapa[x][y+1] = "p"
                        self.mapa[x][y] = 0
                        y = y+1
                        clear_output(wait=True)
                    elif self.mapa[x][y+1] == 1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla 1, ha ganado.")
                        return False
                    elif self.mapa[x][y+1] == -1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla -1, el juego ha terminado.")
                        return False
                    elif self.mapa[x][y+1] == -50:
                      clear_output(wait=True)
                      print("Ha caido en lava, el juego ha terminado.")
                      return False
                # Izquierda
                elif action == 2:
                    if y-1 < 0 or self.mapa[x][y-1] == None:
                        clear_output(wait=True)
                        print("Accion invalida, hay un muro ahi.")
                        continue
                    if self.mapa[x][y-1] == 0:
                        self.mapa[x][y-1] = "p"
                        self.mapa[x][y] = 0
                        y = y-1
                        clear_output(wait=True)
                    elif self.mapa[x][y-1] == 1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla 1, ha ganado.")
                        return False
                    elif self.mapa[x][y-1] == -1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla -1, el juego ha terminado.")
                        return False
                    elif self.mapa[x][y-1] == -50:
                      clear_output(wait=True)
                      print("Ha caido en lava, el juego ha terminado.")
                      return False
                # Abajo
                elif action == 3:
                    if x+1 >= len(self.mapa) or self.mapa[x+1][y] == None:
                        clear_output(wait=True)
                        print("Accion invalida, hay un muro ahi.")
                        continue
                    if self.mapa[x+1][y] == 0:
                        self.mapa[x+1][y] = "p"
                        self.mapa[x][y] = 0
                        x = x+1
                        clear_output(wait=True)
                    elif self.mapa[x+1][y] == 1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla 1, ha ganado.")
                        return False
                    elif self.mapa[x+1][y] == -1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla -1, el juego ha terminado.")
                        return False
                    elif self.mapa[x+1][y] == -50:
                      clear_output(wait=True)
                      print("Ha caido en lava, el juego ha terminado.")
                      return False
                # Arriba
                elif action == 4:
                    if x-1 < 0 or self.mapa[x-1][y] == None:
                        clear_output(wait=True)
                        print("Accion invalida, hay un muro ahi.")
                        continue
                    if self.mapa[x-1][y] == 0:
                        self.mapa[x-1][y] = "p"
                        self.mapa[x][y] = 0
                        x = x-1
                        clear_output(wait=True)
                    elif self.mapa[x-1][y] == 1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla 1, ha ganado.")
                        return False
                    elif self.mapa[x-1][y] == -1:
                        clear_output(wait=True)
                        print("Se llegó a la casilla -1, el juego ha terminado.")
                        return False
                    elif self.mapa[x-1][y] == -50:
                      clear_output(wait=True)
                      print("Ha caido en lava, el juego ha terminado.")
                      return False
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")
        return True

    #-----------------------------------------------------
    def automatico(self):
      x = 3
      y = 0
      action = 1
      while True:
          try:
              for i in range(4):
                  print(self.mapa[i])
              time.sleep(1)
              # Derecha
              if action == 1:
                  if y+1 >= len(self.mapa) or self.mapa[x][y+1] == None:
                      clear_output(wait=True)
                      print("Accion invalida, hay un muro ahi.")
                      action = 4
                      continue
                  if self.mapa[x][y+1] == 0:
                      self.mapa[x][y+1] = "p"
                      self.mapa[x][y] = 0
                      y = y+1
                      action = 4
                      clear_output(wait=True)
                  elif self.mapa[x][y+1] == 1:
                      clear_output(wait=True)
                      print("Se llegó a la casilla 1, ha ganado.")
                      return False
                  elif self.mapa[x][y+1] == -1:
                      clear_output(wait=True)
                      print("Se llegó a la casilla -1, el juego ha terminado.")
                      return False
                  elif self.mapa[x][y+1] == -50:
                      clear_output(wait=True)
                      print("Ha caido en lava, el juego ha terminado.")
                      return False
              # Arriba
              elif action == 4:
                  if x-1 < 0 or self.mapa[x-1][y] == None:
                      clear_output(wait=True)
                      print("Accion invalida, hay un muro ahi.")
                      action = 1
                      continue
                  if self.mapa[x-1][y] == 0:
                      self.mapa[x-1][y] = "p"
                      self.mapa[x][y] = 0
                      x = x-1
                      action = 1
                      clear_output(wait=True)
                  elif self.mapa[x-1][y] == 1:
                      clear_output(wait=True)
                      print("Se llegó a la casilla 1, ha ganado.")
                      return False
                  elif self.mapa[x-1][y] == -1:
                      clear_output(wait=True)
                      print("Se llegó a la casilla -1, el juego ha terminado.")
                      return False
                  elif self.mapa[x-1][y] == -50:
                      clear_output(wait=True)
                      print("Ha caido en lava, el juego ha terminado.")
                      return False
          except ValueError:
              print("Entrada no válida. Intente de nuevo.")
      return True

    def play(self, estado):
      while True:
        try:
            i = int(input("Politica Humana(1) o Automatica(2)?: "))
            if i == 1:
              if not self.jugar():
                break
            if i == 2:
              if not self.automatico():
                break
        except ValueError:
          print("Entrada no válida. Intente de nuevo.")
