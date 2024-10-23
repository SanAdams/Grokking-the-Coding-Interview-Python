def find_duplicate(nums):
  slow = 0
  fast = 0
  
  # Keep going until we find detect a cycle
  while True:
    slow = nums[slow]
    fast = nums[fast]
    fast = nums[fast]
    if nums[slow] == nums[fast]:
      break
  
  # Start slow from the beginning 
  slow = 0
  
  # Advance them both one step at a time until they meet again, that's where the duplicate will be
  while nums[fast] != nums[slow]:
    slow = nums[slow]
    fast = nums[fast]
    
  return nums[fast]
  
print(find_duplicate([3,4,4,4,2])) # Expecting 4, Actual: 4
print(find_duplicate([1,1])) # Expecting 1, Actual: 1
print(find_duplicate([1,3,4,2,2])) # Expecting 2, Actual: 2
