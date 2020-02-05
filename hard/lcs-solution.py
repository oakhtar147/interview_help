# Find the longest common subsequence between two strings.  ie. for “abcde” and
# “acccde” the longest common subsequence is “acde”.


def longest_subsequence(string1, string2):
    """Takes two strings as arguments and returns their longest common subsequence"""
    try:
        subseq = []
        for letter in string1:
            if (letter in string2) and (letter not in subseq):
                subseq.append(letter)
        return "".join(subseq)
    except Exception as e:
        return "Pass in strings only"


print(longest_subsequence(1221, 2121))  # raises exception
print(longest_subsequence("AGGTAB", "GXTXAYB"))  # returns AGTB
