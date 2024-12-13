# This: https://leetcode.com/problems/minimum-window-substring/description/

def minimum_window_substring(string: str, pattern: str) -> str:
    start = end = 0
    min_substring = ""
    freq_substring = {}
    freq_pattern = {}

    # Initialize the freq map for the pattern
    for char in pattern:
        freq_pattern[char] = 1 + freq_pattern.get(char, 0)


    while(end != len(string)):
        
        pass
    
    return min_substring