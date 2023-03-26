#exercise 02

#1
numbers = [1, 2, 3, 4, 5, 7, 7]
integer = 8

def count_integer (numbers, integer):
    count = 0
    for i, num in enumerate(numbers):
        if num == integer:
            count += 1
    if count == 0:
        return 42
    else:
        return count

print(count_integer(numbers, integer))


#2
def list_func(numbers, integer):
    if integer not in numbers:
        return []

    numbers_copy = numbers.copy()

    index = numbers_copy.index(integer)
    numbers_copy[index] = 6

    reversed_list = list(reversed(numbers_copy))

    print(reversed_list)
    return numbers_copy

numbers = [1, 2, 3, 4, 5]
integer = 3
result = list_func(numbers, integer)
print(result)

#3
list1 = [1, 2, 3, 50, 11, 6, 10, 23]
list2 = [11, 5, 8, 3, 4, 1, 50, 7, 2]

def compare_lists (list1, list2):
    new_list = []
    for element in list1:
        if element in list2:
            new_list.append(element)
    return new_list

new_list = compare_lists(list1, list2)
print(new_list)

#4
def remove_duplicates(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

my_list = [2, 3, 8, 5, 3, 2, 8, 3,]

unique_list = remove_duplicates(my_list)
print(unique_list)

#5
def dict_func (dictionary):
    type = dictionary.get("Type", "unknown type")
    brand = dictionary.get("Brand", "unknown brand")
    price = dictionary.get("Price", "unknown price")
    print(f"You have a {type} from {brand} that costs {price}.")
    dictionary["OS"] = "Linux"
    print(dictionary)
    return(dictionary)

dict1 = {"Type": "Smartphone", "Brand": "Samsung", "Price": "1000"}
my_dict = dict_func(dict1)
