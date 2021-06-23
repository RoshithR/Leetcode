# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def validParenthesis(s):
    stack = []
    mapping = {")":"(","}":"{","]":"["}
    for char in s:
        if char in mapping:
            top_most = stack.pop() if stack else '#'
            if mapping[char]!=top_most:
                return False
        else:
            stack.append(char)
    return not stack





s = "([)]"
s="()"
print(validParenthesis(s))