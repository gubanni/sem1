import numpy as np
def InputNumber(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sortmas(mas, m):
    mas2 = []
    for i in mas:
        for i2 in i:
            mas2.append(i2)
    mas=sorted(mas2)
    for x in range(0, len(mas), m):
        e_c = mas[x : m + x]
        if len(e_c) < m:
            e_c = e_c + [None for y in range(x - len(e_c))]
        print(list(e_c))

n = InputNumber("Введите количество строк: ")
m = InputNumber("Введите количество столбцов: ")
mas = np.random.randint(1, 11, size=(n, m))
print(mas)
sortmas(mas, m)
