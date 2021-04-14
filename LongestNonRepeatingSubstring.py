#Given a string s, find the length of the longest substring without repeating characters.

def longest_substr(s):
    max_len, start_indx = 0,0
    char_dict={}
    for i in range(len(s)):
        if s[i] in char_dict:
            start_indx = max(start_indx, char_dict[s[i]]+1)
        max_len = max(max_len, i-start_indx+1)
        char_dict[s[i]]=i
    return max_len


s = 'abcabc'
s='bbbb'
s=" "
print(longest_substr(s))