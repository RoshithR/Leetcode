

# get the longest palindrome, l, r are the middle indexes
# from inner to outer
# def helper(s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1;
#         r += 1
#     return s[l + 1:r]
#
# def longestPalindrome(s):
#     res = ""
#     for i in range(len(s)):
#         # odd case, like "aba"
#         tmp = helper(s, i, i)
#         if len(tmp) > len(res):
#             res = tmp
#         # even case, like "abba"
#         tmp = helper(s, i, i+ 1)
#         if len(tmp) > len(res):
#             res = tmp
#     return res


# def longestPalindrome(s):
#     res=""
#     resLen = 0
#     for i in range(len(s)):
#         #odd length
#         l,r =i,i
#         while l>=0 and r<len(s) and s[l]==s[r]:
#             if (r-l+1)>resLen:
#                 res=s[1:r+1]
#                 resLen = r-1+1
#             l-=1
#             r+=1
#
#             # even length
#             l,r=i,i+1
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 if (r-l+1)>resLen:
#                     res=s[1:r+1]
#                     resLen = r-1+1
#                 l-=1
#                 r+=1
#     return res

def longestPalindrome(s):
    resLen = 0
    res = ""
    # for odd number of characters
    for i in range(len(s)):
        l,r = i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>resLen:
                resLen = r-l+1
                res = s[l:r+1]
            l-=1
            r+=1

    #for even number of characters

        l,r = i, i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if resLen<(r-l+1):
                resLen = r-l+1
                res = s[l:r+1]
            l-=1
            r+=1
    return res


s = "babad"
s="cbbc"
# s="abcd"
print(longestPalindrome(s))


