#The problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def longest_substring_without_repeat(string: str) -> int:
    start = 0
    char_position_map = {}
    max_length = 0

    for end in range(len(string)):
        current_char = string[end]

        # If we encounter a repeat, shrink the window to exclude the earliest occurence of the repeat character in our window
        if current_char in char_position_map and char_position_map[current_char] >= start:
            start = char_position_map[current_char] + 1
        
        char_position_map[current_char] = end
        current_length = end - start + 1
        max_length = max(max_length, current_length)
        
    return max_length

def main():
    string = [
        "abcabcbb",
        "pwwkew",
        "bbbbb",
        "ababababa",
        "",
        "ABCDEFGHI",
        "ABCDEDCBA",
        "AAAABBBBCCCCDDDD",
    ]
    for i in range(len(string)):
        print(i + 1, ". \t Input String: ", string[i], sep="")
        print("\t Length of longest substring: ",
                (longest_substring_without_repeat(string[i])))
        print("-" * 100)


if __name__ == "__main__":
    main()