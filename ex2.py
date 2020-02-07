import sys

def create_fibo(item_a, item_b, length):
    fibo = []
    for i in range(2, length):
        print(i)
        fibo[i] += fibo[i-2] + fibo[i-1]
    return fibo


if __name__ == "__main__":
    result = create_fibo(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    print(result)