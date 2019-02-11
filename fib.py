# Print fibonacci series up to n

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)


# Return the N number of fibonacci series

def fib1(n):
    a, b = 0, 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib1(n-2) + fib1(n-1)

#fib1(10)

# Print first N fibonacci numbers

def fib2(n):
    for i in range(n):
        print(fib1(i))

fib2(10)
