def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# output: SyntaxError: non-default argument follows default argument
