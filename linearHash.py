# Ogni cella è una mappa di chiave, valore
class Cell:
    key = ""
    value = 0

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def set(self, value):
        self.value = value

    def output(self):
        print("'" + self.key + "' : '" + self.value + "'")


class LinearHashTable:
    bucket = []
    keys = set([])
    size = 0
    __loadSum = 0
    __loadFactor = 0.0
    __collisions = 0

    def __init__(self, size):
        self.keys = set([])
        self.size = size
        self.bucket = [None] * size
        self.__loadCalc()

    # Calcola il fattore di caricamento per ogni inserimento o cancellazione
    def __loadCalc(self):
        if self.size == 0:
            self.__loadFactor = 0
        else:
            self.__loadFactor = self.__loadSum / self.size

    # Aumenta il numero di collisioni totali quando è True e lo decrementa quando è False
    def __collision(self, add):

        if add:
            self.__collisions += 1
        else:
            self.__collisions -= 1

    def get(self, k):
        k = str(k)
        if k in self.keys:
            i = 0
            # Usa la funzione di hash in python
            hashed = (hash(k) + i) % self.size
            while self.bucket[hashed] is not None:
                if self.bucket[hashed].key != k:
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    return self.bucket[hashed].value
            return None
        else:
            return None

    def insert(self, k, v):
        k = str(k)
        if k in self.keys:
            i = 0
            hashed = (hash(k) + i) % self.size
            while self.bucket[hashed] is not None:
                if self.bucket[hashed].key != k:
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    self.bucket[hashed].value = v
                    self.__collision(True)
                    return True
        elif self.__loadFactor == 1.0:
            return False
        else:
            newCell = Cell(k, v)
            i = 0
            hashed = (hash(k) + i) % self.size
            while self.bucket[hashed] is not None:
                hashed = (hash(k) + i) % self.size
                i += 1
            self.bucket[hashed] = newCell
            self.keys.add(k)
            self.__loadSum += 1
            self.__loadCalc()
            return True

    # Torna al valore cancellato
    def delete(self, k):
        k = str(k)
        if k in self.keys:
            i = 0
            hashed = (hash(k) + i) % self.size
            while self.bucket[hashed] is not None:
                if self.bucket[hashed].key != k:
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    tmp = self.bucket[hashed].value
                    self.bucket[hashed] = None
                    self.keys.remove(k)
                    self.__loadSum -= 1
                    self.__loadCalc()
                    self.__collision(False)
                    return tmp
            return None
        else:
            return None

    # Torna al fattore di caricamento
    def loadF(self):
        return self.__loadFactor

    # Torna al numero totale di collisioni
    def collisions(self):
        return self.__collisions
