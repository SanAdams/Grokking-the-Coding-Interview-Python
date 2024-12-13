def longest_repeating_character_replacement(string: str, k: int) -> int:
    start = end = 0
    length_max_substring = -1
    highest_frequency = 0
    freq = {}

    while(end != len(string)):

        # Update the frequency of the current character
        freq[string[end]] = 1 + freq.get(string[end], 0)
        
        highest_frequency = max(freq.values())

        # If we need to replace too many characters for this substring, shrink its window until that's not the case
        while end - start + 1 - highest_frequency > k and start < end:
            freq[string[start]] -= 1
            start += 1

        length_max_substring = max(length_max_substring, end - start + 1)
        end += 1
    

    return length_max_substring

# Driver code
def main():
    input_strings = ["aabccbb", "abbcb", "abccde", "abbcab", "bbbbbbbbb"]
    values_of_k = [2, 1, 1, 2, 4]

    for i in range(len(input_strings)):
        print(i+1, ".\tInput String: ", input_strings[i], sep="")
        print("\tk: ", values_of_k[i], sep="")
        print("\tLength of longest substring with repeating characters: ", longest_repeating_character_replacement(input_strings[i], values_of_k[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()

