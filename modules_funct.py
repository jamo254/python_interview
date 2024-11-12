#Challenge 1
#Greatest Common Divisor
import math
def gcd(a,b):
    return math.gcd(a,b)

print(gcd(12,18))
print(gcd(36,60))


#Challenge 2
#Calculate SinCosTan(); takes number x and returns sin(x), cos(x), tan(x)

def sin_cos_tan(x):
    return math.sin(x), math.cos(x), math.tan(x)

print(sin_cos_tan(0))
print(sin_cos_tan(math.pi/2))
print(sin_cos_tan(math.pi))

import math
def calculateSinCosTan(x):
  #write your function here
  sine = math.sin(x)
  cos = math.cos(x)
  tan = math.tan(x)
  return [sine, cos, tan]

print(calculateSinCosTan(0))
print(calculateSinCosTan(math.pi/2))
print(calculateSinCosTan(math.pi))

#Challenge 3
#Implement  the findMax() function; takes a list of numbers and returns the maximum number  
def findMax(numbers):
    return max(numbers)

print(findMax([1,2]))

#Second Solution
def findMaximum(x, y):
    max = 0
    if x > y:
        max = x
    else:
        max = y
    return max

print("Finding maximum of 1 and 2:", findMaximum(1,2))

#Challenge 4 
#Check if a number is divisible by another number
def isDivisible(a,b):
    return a % b == 0

print(isDivisible(10,2))
print(isDivisible(10,3))

# Solution 2
def isDivisibleBy(a,b):
    
    if(a % b == 0):
        return True
    else:
        return False

print(isDivisibleBy(10,2))
print(isDivisibleBy(10,3)) 

#Challenge 5
#Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5)) 

