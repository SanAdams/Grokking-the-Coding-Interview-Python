def maximum_average_subarrayI(nums, k):
    sum = 0
    max_sum = float('-inf')

    for i in range(len(nums)):
        sum += nums[i]

        if i >= k - 1:
            max_sum = max(max_sum, sum)
            sum -= nums[i - (k - 1)]
    
    return max_sum / k

def main():
    input_data = [
        ([10, 5, 2, -1, 6, 3, -2, -4, 4, 1, -3, -6, -1, -2, -5, -7], 4),
        ([7, 3, 1, -2, 6, 2, -1, -3, 4, 1, -2, -5, 2, 0, -4, -6], 4),
        ([12, 9, 5, 2, 8, 6, 4, 1, 7, 5, 3, 0, 4, 2, 0, -3], 4),
        ([-10, -11, -12, -13, -20, -21, -22, -23, -30, -31, -32, -33, -40, -41, -42, -43], 4),
        ([5, 3, -2, -3, 4, 2, -3, -4, 3, 1, -4, -5, 2, 0, -5, -6], 4),
        ([0,1,2,0,4,2],4)
    ]
    
    for i, (nums, k) in enumerate(input_data):
        result = maximum_average_subarrayI(nums, k)
        print(f"{i + 1}.\tInput: nums = {nums}, k = {k}")
        print(f"\tMaximum Average: {result:.2f}")
        print('-' * 100)

if __name__ == "__main__":
    main()