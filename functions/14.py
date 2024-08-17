def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

'''
All identifiers:
- multiply (function)
- get_num (function)
- first_number (variable)
- second_number (variable)
- product (variable)
- prompt (parameter)
- left (parameter)
- right (parameter)
'''
