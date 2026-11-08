class Node:
    def __init__ (self, item, R = None, L = None):
        self.item = item
        self.right = R
        self.left = L


class Bag:
    def __init__(self, items = 4):
        tablesize = 2 * items
        while not self.IsPrime(tablesize):
            tablesize += 1;
        self.table = [None] * tablesize
        self.tablesize = tablesize

        self.size = 0

    def Insert(self, item):
        if (self.size / self.tablesize) >= 0.75:
            self.Resize()

        if self.Exists(item):
            return False

        key = hash(item)
        i = key % self.tablesize

        while self.table[i] is not None:
            i = (i + 1) % self.tablesize
        self.table[i] = item
        self.size += 1
        return True
    
    def Resize(self):
        old_table = self.table
        new_size = self.tablesize * 2
        while not self.IsPrime(new_size):
            new_size += 1
        self.table = [None] * new_size
        self.tablesize = new_size

        for item in old_table:
            if item is not None:
                key = hash(item)
                i = key % self.tablesize
                while(self.table[i] is not None):
                    i = (i+ 1) % self.tablesize
                self.table[i] = item

    def IsPrime(self, num):
        if num == 0:
            return False
        elif num == 1:
            return False
        else:
            i = 2
            while i <= num / 2: # you only have to to do halve
                if num % i == 0:
                    return False
                i += 1
        return True

    def Exists(self, item):
        key = hash(item)
        i = key % self.tablesize
        while(True):
            if self.table[i] == None:
                return False
            if self.table[i] == item:
                return True
            i = (i+1) % self.tablesize

    def Size(self):
        count = 0
        for item in self.table:
            if item:
                count += 1
        return count

    
    def __iter__(self):
        for item in self.table:
            if item:
                yield item

        
    def Delete(self, item):
        if self.Exists(item) == False:
            return False
        
        key = hash(item)
        i =  key % self.tablesize

        while True:
            if self.table[i] == item:
                self.table[i] = False
                return True
            i = (i + 1) % self.tablesize
            
    def Retrive(self, item):
        if self.Exists(item) == False:
            return None
        
        key = hash(item)
        i = key % self.tablesize
        
        while self.table[i] is not None:
            if self.table[i] == item:
                return self.table[i]
            i = (i + 1) % self.tablesize
        return None