def isHappy(n):
    # Separate a number into its digits
    # Iterate through and square then sum
    # Store the numbers already visited
    # If it's a 1 at any point, then it's happy
    # Else if the number has already been visited, it's not a happy number

    visited = []
    digits = breakNumberIntoDigits(n)
    new_number = 0

    visited.append(n)
    while new_number != 1:
        new_number = sumOfSquaresOfDigits(digits)
        digits = breakNumberIntoDigits(new_number)

        if new_number in visited:
            return False
        elif new_number == 1:
            return True
        else:
            visited.append(new_number)

        new_number = 0

def sumOfSquaresOfDigits(digits):
    sum_ = 0
    for i in range (len(digits)):
        sum_ += (digits[i] * digits[i])
    return sum_

def breakNumberIntoDigits(num):
    digits = []

    if num < 10:
        digits.append(num)
        return digits

    while num >= 10:
        digits.append(num % 10)

        # Take off the last digit
        num //= 10
    
    digits.append(num)
    return digits

# print(isHappy(0)) # Expecting False
# print(isHappy(10)) # Expecting True
# print(isHappy(28)) # Expecting True
# print(isHappy(8)) # Expecting False

#=============================================== Above is the bruteforce solution, below is an optimized solution ================================================


# The idea is to use a fast pointer to go through the square sums quickly and if it ever meets the slow pointer, 
# it means there's a cycle and the number is not happy, other wise if the fast pointer reaches 1, then the number is happy
def isHappyOptimal(num):
    slow_pointer = num
    fast_pointer = squareSum(squareSum(num))

    while fast_pointer != 1 and fast_pointer != slow_pointer:
        
        # Perform the square sum operation once for slow pointer
        slow_pointer = squareSum(slow_pointer)

        # Perform the square sum operation twice for fast pointer
        fast_pointer = squareSum(squareSum(fast_pointer))

    return fast_pointer == 1

def squareSum(n):
    sum_ = 0
    while n != 0:
        remainder = n % 10
        sum_ += remainder * remainder
        n //= 10
    return sum_
    

print(isHappyOptimal(0)) # Expecting False
print(isHappyOptimal(10)) # Expecting True
print(isHappyOptimal(28)) # Expecting True
print(isHappyOptimal(8)) # Expecting False