"""
Дано число a>1. Определить каким по счету числом Фибоначчи оно является.
Если не является, то "-1".
"""

i = 1
fib = 0
fib_new = 1
temp = 0
number = int(input("Введите число: "))
while fib_new <= number:
 #   temp = fib_new
  #  fib_new = temp + fib
   # fib = temp
    fib, fib_new = fib_new, fib + fib_new
    i = i+1
#print (fib_new, i)    
if fib == number:
   print (f"Является {i} по счету числом Фибоначи")
else:
   print (-1)