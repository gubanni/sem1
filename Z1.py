def InputNumber():
    is_OK = False
    while not is_OK:
        try:
            number = int(input("Введите число: "))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Да")
    elif 0 < num < 6:
        print("Нет")
    else:
        print("число вне пределов 7 дней")


num = InputNumber()
checkNumber(num)