import time

    
# def fib(n,a=0, b=1):
#     if n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         return fib(n - 1, b, a + b)
    

# def fib(n):
#     if n<=1: return 1
#     else: return fib(n-1)+fib(n-2)
start = time.time()
a = 0
b = 1 
for x in range(41):
    temp = b
    b += a
    a = temp    
print(a)
print(time.time()-start)