#generator function
def fibonacci_s():
    a = 0
    b = 1

    while True:
        c = a
        a = b
        b = c + a

        yield c


fib_generator = fibonacci_s()

for i in range(20):
    print(next(fib_generator), end='\n')