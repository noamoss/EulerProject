def palidnrome(num):
    text_num = str(num)     # translate number to string
    num_length = len(text_num)  # calculate the string length
    max_check = num_length // 2  # find the middle location of the string

    i = 0     # initalize the loop pointer

    while i <= max_check :                 # run through the firs half of the stirng
        if text_num[i] != text_num[-1-i]:      # and compare each character to the parallel character 
            return False
        i+=1                               # move to the next character
    return True


a = 999                                 # initalize the counter of the first factor
b = 999                                # initalize the counter of the second factor
largest_palindrome = 0

while a > 100:                             # focus on 3 digits numbers only
    if b>100:                               
        if palidnrome(a*b):                             # if a number is a palindrome
            print(f"{a} * {b} = {a*b}")
            if a*b > largest_palindrome:                    # check if it is bigger than other palindromes produts we found before
                largest_palindrome = a*b                       # if it is bigger, store it
        b = b - 1                                      # run thorugh second factor, until 100
    else:
        a = a-1                                         # once we finished looping through the second factor, lower the first factor by 1
        b = 999                                         # and reinitalize the the second facotr

print(f"largest palindrome: {largest_palindrome}")
