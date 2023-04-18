import time
import random

def get_mean_time(S,x,search):
    t_start = time.time()
    for i in range(5):
        search(S,x)
    t_end = time.time()
    t_total = t_end - t_start
    return t_total/5

def linear_search(S,x):
    for i in range(0,len(S)):
        if S[i] == x:
            return True
    return False

def binary_search(S,x):
    low = 0
    high = len(S)-1
    while low <= high:
        mid = low + (high - low)//2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def fibonacci_search(S, x):
    size = len(S)
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if S[index] < x:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif S[index] > x:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return True
    if (f1) and (S[size - 1] == x):
        return True
    return False

t_linear = []
t_binary = []
t_fibonacci = []
size = 10
for i in range(100):
    S = sorted([random.randint(-10000,10000) for j in range(size)])
    x = random.randint(-10000,10000)
    t_linear.append(get_mean_time(S,x,linear_search))
    t_binary.append(get_mean_time(S,x,binary_search))
    t_fibonacci.append(get_mean_time(S,x,fibonacci_search))
    size+=10
print("List(10 to 1000 size) average execution times: ")
print("linear_search: ",t_linear)
print("binary_search: ",t_binary)
print("fibonacci_search: ",t_fibonacci)
