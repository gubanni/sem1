def inputNumbers(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} число: "))
                a[i] = number
                is_OK = True
            except ValueError:
                print("Введите числа!")
    return a

def inputOperation():
    operation = str(input(f"Введите операцию(варианты:+,-,/,*,mod,pow,div): "))
    return operation

def Calc(numbers, operation):
    if operation == '+':
        print(numbers[0]+numbers[1])
    elif operation == '-':
        print(numbers[0]-numbers[1])
    elif operation == '*':
        print(numbers[0]*numbers[1])
    elif operation == '/':
        try:
            print(numbers[0]/numbers[1])
        except ArithmeticError:
            print("Деление на 0")
    elif operation.lower() == 'mod':
        try:
            print(numbers[0]%numbers[1])
        except ArithmeticError:
            print("Деление на 0")        
    elif operation.lower() == 'div':
        try:
            print(numbers[0]//numbers[1])
        except ArithmeticError:
            print("Деление на 0") 
    elif operation.lower() == 'pow':
        print(numbers[0]**numbers[1])
    else:
        print("Неизвестный оператор")

numbers = inputNumbers(2)
operation = inputOperation()
Calc(numbers, operation)