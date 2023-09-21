#Implement a recursive function to calculate the factorial of a given number
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


number = int(input("Enter a number to calculate its factorial: "))
if number < 0:
  print("Factorial is not defined for negative numbers.")
else:
  result = factorial(number)
  print(f"The factorial of {number} is {result}")
