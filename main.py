# Exercise 01

def selection_sort(numbers: list):
    for fill_slot in range(len(numbers) - 1, 0, -1):
        position_of_max = fill_slot

        for location in range(fill_slot):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location

        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp


my_list = [3, 8, 9, 4, 6, 0, 1, 7, 2, 5]
print(f"my list before sorting {my_list}")
selection_sort(my_list)
print(f"my list after sorting {my_list}")


# Exercise 02

def binary_search(text: list, target: str) -> str:
    first = 0
    last = len(text) - 1

    while first <= last:
        mid = (first + last) // 2
        if text[mid] == target:
            return text[mid]
        else:
            if target < text[mid]:
                last = mid - 1
            else:
                first = mid + 1


text_list = ['apple', 'strawberry', 'mango', 'pineapple', 'cherry', 'banana', 'fig']
result = binary_search(text_list, 'apple')
print(result)


# Exercises 3-6

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __my_hash(self, key):
        if type(key) == int:
            return key % self.size
        elif type(key) == str:
            return len(key) % self.size
        else:
            return None

    def put(self, key, data):
        hash_value = self.__my_hash(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] is key:
                self.data[hash_value] = data
            else:
                next_slot = (hash_value + 1) % self.size
                while self.slots[next_slot] is not None and self.slots[next_slot] is not key:
                    next_slot = (next_slot + 1) % self.size
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        hash_value = self.__my_hash(key)
        if self.slots[hash_value] == key:
            return self.data[hash_value]
        else:
            next_slot = (hash_value + 1) % self.size
            while next_slot != hash_value:
                if self.slots[next_slot] == key:
                    return self.data[next_slot]
                next_slot = (next_slot + 1) % self.size
            return None

