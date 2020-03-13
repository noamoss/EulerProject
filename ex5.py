def find_factors(num):
    """ find all relevant factors between 1 and a num variable, not including sub-divided numbers"""
    results = set()
    for i in range (num, 1, -1):
        if not(included(i, results)):
            results.add(i)
    return results

def included(num, set_to_check):
    """ check if the number can be overlooked when iterating over a given set"""
    for a in set_to_check:
        if (a % num == 0 and a!=1) or num**2 == a:
            return True
    return False


factors_to_check = find_factors(20) # minimize the checks by checking only relevant factors

i = 1    
stop_check = None

while stop_check != True:
    stop_check = None
    i += 1
    for num in factors_to_check:
        if i % num != 0:
            stop_check = False
    if stop_check == None:
        print(f"Found: {i}")
        stop_check = True
        break