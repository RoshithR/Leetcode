# Given two strings s and t, return the minimum window in s which will contain all the characters in t.
# If there is no such window in s that covers all characters in t, return the empty string "".
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

from collections import Counter
# The worst possible O(N^2) solution
# def MinWindow(s, t):
#     lookup = Counter(t)
#     result = ""
#     n = len(s)
#     max_len = float("inf")
#
#     def helper(substr):
#         for k,v in lookup.items():
#             if k not in substr or substr[k]<v:
#                 return False
#         return True
#
#     for start in range(n):
#         for end in range(n):
#             substr_lookup = Counter(s[start:end+1])
#             if helper(substr_lookup):
#                 if len(s[start:end+1])<max_len:
#                     max_len = len(s[start:end+1])
#                     result = s[start:end+1]
#     return result, max_len

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


if __name__=="__main__":
    s = "ADOBECODEBANC"
    # s = "BANC"
    # s = 'ab'
    t = "ABC"
    # t='a'
    print(minWindow(s,t))