# For the problem Circular Array Loop, I want to check if my array traversal is correct

nums = [1,2,3,4,5,6]

fast = 0
slow = 0
len_ = len(nums)
for i in range(10):
    slow += nums[slow]
    if slow > len_:
        slow %= len(nums)
        slow -= 1
    print(f"slow: {slow}")


    fast += nums[fast]
    if fast > len_:
        fast %= len(nums) 
        fast -= 1
    fast += nums [fast]
    if fast > len_:
        fast %= len(nums) 
        fast -= 1
    print(f"fast: {fast}")

# Looks like my traversal is correct
# Unfortunately I didn't realize that you have examine the start of for this problem. I had this really weird idea that every cycle
# visits every element. Not true :)
# This traversal only works if all the numbers are positive, which makes it half correct(wrong)