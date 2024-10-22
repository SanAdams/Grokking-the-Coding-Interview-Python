def circular_array_loop(nums):  
  length = len(nums)
  
  # Try finding a cycle starting from every element
  for i in range (length):
    slow = i
    fast = i
    
    # True for positive direction, false for negative direction
    direction = nums[i] > 0
    
    while True:
      slow = next_step(slow, nums[slow], length)
      curr_direction = nums[slow] > 0
      if curr_direction is not direction or (abs(nums[slow] % length) == 0):
        break
      
      
      fast = next_step(fast, nums[fast], length)
      curr_direction = nums[fast] > 0
      # If the direciton changes or the number at the pointer is a multiple of the length
      # of the array, the this starting point will not result in a valid caycle
      if curr_direction is not direction or (abs(nums[fast] % length) == 0):
        break
      
      
      fast = next_step(fast, nums[fast], length)
      curr_direction = nums[fast] > 0
      if curr_direction is not direction or (abs(nums[fast] % length) == 0):
        break
      
      if slow == fast: return True
      
  return False
    
    
def next_step(pointer, value, length):
  # Keep the result in bounds
  res = (pointer + value) % length
  if res < 0: res += length
  return res

