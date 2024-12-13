from typing import List


def findRepeatedDnaSequences(s: str, k: int) -> List[str]:
    SEQUENCE_LENGTH = k
    res = []
    sequences = {}
    right = SEQUENCE_LENGTH
    left = 0
    length = len(s)

    if length < SEQUENCE_LENGTH:
        return []
    
    while right <= length:
        current_sequence = s[left:right]

        if current_sequence in sequences:
            if sequences[current_sequence] == 1:
                res.append(current_sequence)
            sequences[current_sequence] += 1
        else:
            sequences[current_sequence] = 1
        
        left += 1
        right += 1
    return res


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", 10))