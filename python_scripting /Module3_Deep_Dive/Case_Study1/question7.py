# Write a program which can compute the factorial of a given numbers. Use recursion to find it.
# Hint: Suppose the following input is supplied to the program:
# 8
# Then, the output should be: 40320

# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 8

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
