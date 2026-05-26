def factorial(f):
    if f == 0:
        return 1
    return f * factorial(f-1)

def sumation(f):
    if f == 0:
        return 1
    return f + sumation(f-1)

def exponential(base, power):
    if power == 0:
        return 1
    return base * exponential(base, power-1)

def fibonacci(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    return fibonacci(f-1) + fibonacci(f-2)

def sum_digits(f):
    f = str(f)

    if f == '':
       return 0
    return int(f[0]) + sum_digits(f[1:])

def reverse_digits(f):
    f = str(f)

    if f == '':
       return f
    return int(f[-1] + str(reverse_digits(f[:-1])))

print(reverse_digits(15732))
def product_digits(f):
    if f == 0:
        return 1
    
def number_product(f, n):
    if n == 0:
        return 0
    return f + exponential(f, n-1)

def sum_of_numbers_range(f,n):
    if f == n:
        return f 
    return f + sum_of_numbers_range(n, f-1)




