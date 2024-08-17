def number_range(n):
    if n in range(51):
        return "the number is between 0 and 50"
    elif n in range(51,101):
        return "the number is between 51 and 100"
    elif n > 100:
        return "the number is greater than 100"
    else:
        return "the number is less than 0"

print(number_range(50))
print(number_range(51))
print(number_range(100))
