def diet_plan_performance(calories, k, lower, upper):
    sum = 0
    left = 0
    right = left + k - 1
    points = 0
    
    for i in range(left, right + 1): 
      sum += calories[i]

    points += determine_points(sum, upper, lower)
    
    while right < len(calories) - 1:
      sum -= calories[left]
      left += 1
      right += 1
      sum += calories[right]
      points += determine_points(sum, upper, lower)
      
    return points
  
def determine_points(sum, upper, lower):
    if sum < lower:
      return -1
    elif sum > upper:
      return 1
    else:
      return 0