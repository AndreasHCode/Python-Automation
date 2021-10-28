def divide42(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Can't divide by zero")

print(divide42(4))
print(divide42(42))
print(divide42(0))
print(divide42(-1))
