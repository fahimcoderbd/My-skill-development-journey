import math

N = int(input())

if 0 < N < 1000:

    def big_factorial(num):

        factorial = math.factorial(num)
        last4 = factorial % 10000
        
        if factorial < 10000:
            return last4
        else:
            return f"{last4:04d}"

    print(big_factorial(N))