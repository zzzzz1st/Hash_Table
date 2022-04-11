# il singolo componente di linked list
class Node:
    def __init__(self, key, value, nextel=None):
        self.key = key
        self.value = value
        self.next = nextel


# Definizione di linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtFirst(self, key, value):
        self.head = Node(key, value, self.head)
        self.size += 1

    def insertAtLast(self, key, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(key, value)
        self.size += 1

    def remove(self, key):
        current = self.head
        if current.key == key:
            self.head = current.next
        else:
            while current.next:
                previous = current
                current = current.next
                if current.key == key:
                    previous.next = current.next
            self.size -= 1

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def printAll(self):
        current = self.head
        while current:
            print(current.key, current.value)
            current = current.next


class ChainedHashTable:
    __loadSum = 0
    __loadFactor = 0.0
    __collisions = 0

    def __init__(self, size):
        self.table = [None] * size
        self.size = size

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

    # Se non c'è nessun elemento inizializza un linked list e inserisce il primo elemento
    def insert(self, k, value):
        hashed = hash(k) % self.size
        if self.table[hashed] is None:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(k, value)
            self.table[hashed] = newLinkedList
            self.__loadSum += 1
            self.__loadCalc()
        else:
            self.table[hashed].insertAtLast(k, value)
            self.__collision(True)

    def get(self, k):
        hashed = hash(k) % self.size
        if self.table[hashed] is not None:
            return self.table[hashed].find(k)

    def delete(self, k):
        hashed = hash(k) % self.size
        if self.table[hashed] is not None:
            if self.table[hashed].size > 1:
                self.__collision(False)
            elif self.table[hashed].size == 1:
                self.__loadSum -= 1
                self.__loadCalc()
            self.table[hashed].remove(k)

    def loadF(self):
        return self.__loadFactor

    # Torna al numero totale di collisioni
    def collisions(self):
        return self.__collisions
