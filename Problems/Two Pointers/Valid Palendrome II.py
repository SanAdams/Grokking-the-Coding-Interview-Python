def is_palindrome(string):
  
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            left_mismatch_index = left
            right_mismatch_index = right
            possible_from_left_side = True
            possible_from_right_side = True

            # Skip the right character first
            right -= 1
            while(left <= right):
                if string[left] != string[right]:
                    possible_from_right_side = False
                left += 1
                right -= 1

            if possible_from_right_side:
                return True
            
            # Go back to where the mismatch happebed
            left = left_mismatch_index
            right = right_mismatch_index

            # Skip the left character
            left += 1
            while(left <= right):
                if string[left] != string[right]:
                    possible_from_left_side = False
                left += 1
                right -= 1
            return possible_from_left_side or possible_from_right_side
        right -= 1
        left += 1
    return True

# Uhhh if you want to find this problem, it's everywhere just google it.

print(is_palindrome("madame"))
