def pares(n):
    i = 0
    while i < n:
        yield 2 * i
        i += 1
#for n in pares(10):
    #print(n)
#-----------------------------
def impares(n):
    i = 0
    while i < n:
        yield 2 * i + 1
        i += 1
#for n in impares(10):
    #print(n)
#-----------------------------
def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1
#-----------------------------
def aleatorios(n):
    import random
    for i in range(n):
        yield random.random
#-----------------------------
