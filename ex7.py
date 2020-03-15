def isPrime(num):
    """ check if a number is a prime number """
    i = 1
    while i<num:
        if num % i == 0 and i != 1:
            return False
        i=i+1
    return True

def skip_devided(x, sety):
    """ verify if there a need to check a gien number"""
    for y in sety:
        if x % y == 0 and x!=1 and y!=1:
            return True
    return False

def find_prime_by_location(x):
    i = 1
    results = set()
    while len(results) < x:
        i+=1
        if not(skip_devided(i, results)) and isPrime(i):
            results.add(i)
    return max(results)