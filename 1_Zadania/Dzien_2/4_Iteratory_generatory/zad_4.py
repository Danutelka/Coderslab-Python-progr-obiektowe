def fib(n):
    a = 0
    b = 1

    yield a
    yield b

    for x in range(1, n-1):
        b = a + b
        a = b - a
        yield b

for element in fib(5):
    print(element)