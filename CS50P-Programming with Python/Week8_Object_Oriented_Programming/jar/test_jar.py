class Jar:
    def __init__(self, capacity=12):
        if capacity > 12:
            capacity = 12
        if capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError("Jar is full")

    def withdraw(self, n):
        if n <= self._size:
            self._size -= n
        else:
            raise ValueError("Not enough cookies in the jar")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = min(new_capacity, 12)
        if self._size > self._capacity:
            self._size = self._capacity

    @size.setter
    def size(self, new_size):
        if new_size < 0:
            raise ValueError("Size must be non-negative")
        self._size = min(new_size, self._capacity)
