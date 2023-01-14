
def say_hi(number):
    if float(number) > 7:
        print("Привет")

def say_hi_name(name):
    if name == "Вячеслав":
        print("Привет, " + name)
    else:
        print("Нет такого имени")

def get_multiple_of(arr):
    number = tuple(map(int, arr.split(', ')))
    for num in number:
        if ((num % 3) == 0):
            print(num)

def all_tests():
    number = input('Print value of "number" ')
    say_hi(number)
    name = input('Print value of "name" ')
    say_hi_name(name)
    arr = input('Print list of numbers, for ex: "1, 2, 3" ')
    get_multiple_of(arr)
    wait = input("Press Enter to exit.")
