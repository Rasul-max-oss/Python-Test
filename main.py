def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("=== КАЛЬКУЛЯТОР ===")
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f'{x} * {y} = {multiply(x, y)}')
    print(f'{x} / {y} = {divide(x, y)}')

if __name__ == "__main__":
    main()