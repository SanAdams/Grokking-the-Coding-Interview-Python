"""
Statement
Given two strings, str1 and str2, find the shortest substring in str1 such that str2 is a subsequence of that substring.

A substring is defined as a contiguous sequence of characters within a string. A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.

Let’s say you have the following two strings:

str1 = “abbcb”

str2 = “ac”

In this example, “abbc” is a substring of str1, from which we can derive str2 simply by deleting both the instances of the character 
b. Therefore, str2 is a subsequence of this substring. Since this substring is the shortest among all the substrings in which str2 is present as a subsequence, the function should return this substring, that is, “abbc”.

If there is no substring in str1 that covers all characters in str2, return an empty string.

If there are multiple minimum-length substrings that meet the subsequence requirement, return the one with the left-most starting index.
"""

# Produce every substring from smallest to largest, and return the first substring that has the pattern we want (str2)
def minimum_window_subsequence_naive(str1, str2):
    
    len1 = len(str1)
    len2 = len(str2)
    
    for window_size in range(len2, len1 + 1):
      for start in range(len1 - window_size + 1):
        end = start + window_size
        substring = str1[start:end]
        print(substring)
        if is_subsequence(substring, str2):
          return substring
          
    return ""
    
def is_subsequence(string1, string2):
    i = 0
    j = 0
    
    while j < len(string2) and i < len(string1):
        if string2[j] == string1[i]:
            j += 1
        i += 1
    
    return j == len(string2)



def minimum_window_subsequence_optimal():
    return