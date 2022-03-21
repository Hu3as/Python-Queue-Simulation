
from typing import Tuple, List

class Queue:

    def __init__(self):           #konstruktor
        self.size = 5
        self.input = 0            #miejsce zapisu
        self.output = 0           #miejsce odczytu
        self.content = [None for i in range(self.size)]

    def debug_function(self):
        print("current size: ", self.size)
        print("current output ID { shoud be 0 } : ", self.output)
        print("current input ID { shoud point on first free memory cell after saved element } :", self.input+1)

    def realloc(tab, size):

        Oldsize = len(tab)
        for i in range(size):
            if i < Oldsize:
                return tab[i]
            else:
                return None


    def is_empty(self):             #zwraca True jeśli index input = index output
        if self.input == self.output:
            return True
        else:
            return False

    def peek(self):                 #zwraca output #lub None dla pustej kolejki
        return self.content[self.output]

    def dequeue(self):              #zwraca none jak kolejka pusta lub
        pass                        #daną z outputu i przesuwa kolejkę o 1
        if(self.output == self.input):
            return None
        else:
            toRead = self.content[self.output]
            for i in range(1,len(self.content)):
                self.content[i-1] = self.content[i]
            self.input-=1
            return toRead



    def enqueue(self, input_content):              #otrzymujące dane do wstawienia do kolejki
        for i in range(0, len(input_content)):
            if self.input<self.size-1:
                self.content[self.input] = input_content[i]

            else:
                self.size+=5
                for x in range(0,5):
                    self.content.append(None)

                self.content[self.input] = input_content[i]
                #self.input += 1
            self.input += 1


    def select(self):

        print("[", end = '')
        for i in range(self.size-1):
            print(self.content[i], end = ',')
        print(self.content[-1], end='')
        print("]", end='\n')


    def ileNone(self):
        return self.content.count(None)

    def relaseMemory(self):
        timer = 0
        if self.is_empty():
            if self.ileNone() > 5:

                for y in range(0, self.size-5):
                    self.content.remove(None)
                    timer+=1

        else:
            for i in range(self.ileNone()):
                    self.content.remove(None)
                    timer+=1
        self.size=self.size-timer




def main():

    print("___kolejka układa się od lewej do prawej___")
    print("___Jeśli braknie miejsca, następuje dynamiczna alokacja pamięci___")
    #print("___Dodałem również funkcję zwalniającą nieużywaną pamięć (czyszczącą z kolejki wartość 'None' )___")
    #print("___ lub wracająca do stanu początkowego ___")
    kolejka = Queue()

    print("___ Tworzenie pustej kolejki ___")
    kolejka.select()

    print("___ enqueue [1, 2, 3, 4] ___")
    kolejka.enqueue((1, 2, 3, 4))
    kolejka.select()

    print("___ czy kolejka pusta? ___")
    print(kolejka.is_empty())

    print("___ dequeue ___")
    print(kolejka.dequeue())

    print("___ peek ___")
    print(kolejka.peek())

    print("___ testowe wypisanie kolejki ___")
    kolejka.select()

    print("___ enqueue [5, 6, 7, 8] ___")
    kolejka.enqueue((5,6,7,8))
    kolejka.select()

    print("___ opróżnienie kolejki ___")
    for i in range(0, kolejka.input):
        print(" - ",kolejka.dequeue())

    print("___ wypisanie kolejki ___")
    kolejka.select()

    print("___ Czy Kolejka Pusta? ___")
    print(kolejka.is_empty())


main()