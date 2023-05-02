#Question 1
import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
  if n==0 or n==1:
    return n
  else:
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_dynamic(n):
  f = [0,1]
  for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])
  return f[n]
    
t_recursive = []
t_dynamic = []
for n in range(10,101,10):
  if n>=50:
    t_recursive.append(10**4)
  else:
    t_start = time.time()
    fibonacci_recursive(n)
    t_end = time.time()
    t_recursive.append(t_end-t_start)
  t_start = time.time()
  fibonacci_dynamic(n)
  t_end = time.time()
  t_dynamic.append(t_end-t_start)

x = [i for i in range(10,101,10)]
plt.xlabel("n-th Fibonacci Number")
plt.ylabel("Execution time")
plt.plot(x, t_recursive, 'r')
plt.plot(x, t_dynamic, 'b')
plt.legend(['fibonacci_Recursive','fibonacci_Dynamic'])
plt.show()



#Question 2
def fibonacci_recursive(n):
  if n==0 or n==1:
    return n
  else:
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_dynamic(n):
  f = [0,1]
  for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])
  return f[n]

n = 0
while n!=-1:
  try:
    fibonacci_recursive(n)
  except RecursionError as re:
    print("Fibonacci Number is too big.")
    print("The maximum value of n is:",n-1)
    break
  n+=1

try:
  num = fibonacci_dynamic(n)
  print("{}-th Fibonacci number is: {}".format(n,num))
except RecursionError as re:
  print("Fibonacci Number is too big.")
