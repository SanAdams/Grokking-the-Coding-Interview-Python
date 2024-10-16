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
    fast_pointer_digits = breakNumberIntoDigits(num)
    fast_pointer = sumOfSquaresOfDigits(fast_pointer_digits)

    while fast_pointer != 1 or fast_pointer != slow_pointer:
        
        # Perform the square sum operation once for slow pointer
        slow_pointer_digits = breakNumberIntoDigits(slow_pointer)
        slow_pointer = sumOfSquaresOfDigits(slow_pointer_digits)

        # Perform the square sum operation twice for fast pointer
        fast_pointer_digits = breakNumberIntoDigits(fast_pointer)
        fast_pointer = sumOfSquaresOfDigits()
        
        fast_pointer_digits = breakNumberIntoDigits(fast_pointer)
        fast_pointer = sumOfSquaresOfDigits()

        if fast_pointer == 1:
            return True

    return False

print(isHappy(0)) # Expecting False
print(isHappy(10)) # Expecting True
print(isHappy(28)) # Expecting True
print(isHappy(8)) # Expecting False