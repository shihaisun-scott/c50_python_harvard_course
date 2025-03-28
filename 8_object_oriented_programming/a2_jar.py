class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError("Negative number")
        self._capacity = capacity
        self._size = 0

    def __str__(self): # returning a string
        s = self._size * "🍪"
        return s

    def deposit(self, n):
        if n + self._size <= self._capacity:
            self._size += n
        else:
            raise ValueError("Too many cookies")

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError("Too few cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    

def main():
    jar = Jar(5)
    print(jar.capacity)
    jar.deposit(3)
    print(jar)         # 🍪🍪🍪
    print(jar.size)    # 3
    jar.withdraw(2)
    print(jar)         # 🍪
    print(jar.capacity)  # 5

if __name__ == "__main__":
    main()