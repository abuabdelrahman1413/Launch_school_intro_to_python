def factorial(number):
    f = 1
    for i in range(1, number + 1):
        f = f * i
    return f

print(factorial(5))
