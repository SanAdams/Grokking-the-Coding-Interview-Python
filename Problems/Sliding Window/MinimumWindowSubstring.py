# This: https://leetcode.com/problems/minimum-window-substring/description/

def minimum_window_substring(string: str, pattern: str) -> str:
    if not string or pattern:
        return ""

    start = end = 0
    min_substring = ""
    freq_substring = {}
    freq_pattern = {}

    # Initialize the freq map for the pattern
    for char in pattern:
        freq_pattern[char] = 1 + freq_pattern.get(char, 0)

    while(end != len(string)):
        
        min_substring = min_substring if len(min_substring) < end - start + 1 else string[start : end + 1]

        while not are_equal_frequencies(freq_substring, freq_pattern):
            end += 1
            freq_substring[string[end]] = 1 + freq_substring.get(string[end], 0)
            
        while are_equal_frequencies(freq_substring, freq_pattern) and start < end:
            start += 1
            freq_substring[string[start]] -= 1

    return min_substring

def are_equal_frequencies(freq_substring: dict, freq_pattern: dict) -> bool:
    """
    Returns True if all the frequencies in freq_substring are 
    greater than or equal to the frequencies in freq_pattern
    """

    for key, value in freq_pattern.items():
        if freq_substring[key] < value:
            return False
        
    return True