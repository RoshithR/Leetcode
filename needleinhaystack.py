#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#sliding window solution
#The time complexity is O((N-L)L), we compute a substring of length L in a loop that runs (N-L) times

def find_needle(needle,haystack):
    L,n= len(needle), len(haystack)
    for i in range(n-L+1):
        if needle==haystack[i:i+L]:
            return i
    return -1

haystack = "hello"
needle = "ll"
print(find_needle(needle,haystack))