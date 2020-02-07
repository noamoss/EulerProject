import math 

def largest_prime_factor(num):
    if num % 2 == 0:
        max_prime_factor = 2  # in case of an even number, set the initial check on 2 and it's multiplied  number
        num = num / 2
    else:                                
        max_prime_factor = -1   # in case of an even number run over all numbers

    for i in range(3, int(math.sqrt(num)) + 1, 2):  #in both cases we can check only odd numbers (as even numbers are devided by 2 and therefore can not be primary)
        while num % i == 0:                         # if we find a natural factor of the number
            max_prime_factor = i                        # we set it as the biggest factor 
            num = num / i                                # and limit future check as it's the mutiplied number
    
    if num > 2:                                                                  
        max_prime_factor = num                            # we set the bigest prime fact we found (if we found) as returned result
    
    return int(max_prime_factor)


print(largest_prime_factor(600851475143))