# test function
import numpy as np

def fibonacci(n):
    """ This definition returns the first n Fibonacci numbers as numpy array. E.g. calling fibonacci(21)
    returns first 21 Fibonacci numbers """
    fib_nums = np.array([])
    for order in range(n):
        print(order)
        if order == 0:
            fib_nums = np.append(fib_nums, 0)
        elif order == 1:
            fib_nums = np.append(fib_nums, 1)
        else:
            fib_nums = np.append(fib_nums, fib_nums[order - 1] + fib_nums[order - 2])
    fib_nums = fib_nums.astype(int)
    return fib_nums