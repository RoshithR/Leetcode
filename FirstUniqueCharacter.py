# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

import collections
def firstNonRepeatingChar(s):
    char_dict = collections.Counter(s)
    for index,char in enumerate(s):
        if char_dict[char]==1:
            return index
    return -1

s = "loveleetcode"
print(firstNonRepeatingChar(s))