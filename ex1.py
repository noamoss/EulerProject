def devided_by(x, num):
    return num % x == 0

def sum_multiply(a, b,topnum):
    sum = 0
    for i in range(0, topnum):
        if devided_by(3, i) or devided_by(5, i):
            sum += i
    return sum

print(sum)