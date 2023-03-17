#1
def name_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Hello " + name + ". Your age is: " + age)
    return name + age

result = name_age()
print(result)

#2
def swap_integers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return str(num1) + str(num2)

result = swap_integers(10, 20)
print(result)

#3
def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and num1 % 10 == 0 and num2 % 10 == 0:
        return True
    else:
        return False

result = check_numbers(13, 22)
print(result)
result = check_numbers(30, 60)
print(result)

#4
def sum_up(num1, num2):
    if num2 <= num1 or num1 <= 0 and num2 <= 0:
        return 0
    else: result = 0
    for i in range(num1, num2 + 1):
        result += i
    return result

result = sum_up(3, 9)
print (result)


#5
def circle_area(r1, r2, r3):
    pi = 3.142
    area1 = pi * r1 ** 2
    area2 = pi * r2 ** 2
    area3 = pi * r3 ** 2
    return area1 + area2 + area3

result = circle_area(2, 4, 6)
print(result)

#6
def check_string(text):
    if text.lower().startswith('a') or text.lower().endswith('a'):
        return 'True'
    else:
        return 'False'

print(check_string('ANNA'))
print(check_string('anna'))
print(check_string('Hello'))

def triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

print(triangle(20))
