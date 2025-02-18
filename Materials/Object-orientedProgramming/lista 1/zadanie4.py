#
# Lucjan Pucelak
# zadanie 4
# python3 zadanie4.py
#

import numpy as np

def printFloat(j):
        r = round(j,2)

        if len(str(r)) == 3:
            print(f'{r}' + '0', end="")
        else:
            print(f'{r}', end="")

class Tabliczka:
    def __init__(self, x1, x2, y1, y2, skok):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.skok = skok

    def printTabliczka(self):

        print("      ", end="")
        for j in np.arange(self.y1, self.y2, self.skok):
            printFloat(j)
            print(" ", end="")

        print()
        
        for j in np.arange(self.x1, self.x2, self.skok):
            printFloat(j)
            print(':', end=" ")
            
            for i in np.arange(self.y1, self.y2, self.skok):
                iloczyn = i * j
                printFloat(iloczyn)
                print(" ", end="")

            print()  
            
t = Tabliczka(1, 1.3, 0.2, 3.14, 0.3)
t.printTabliczka()