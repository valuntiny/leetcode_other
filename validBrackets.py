'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        ref = {'}':'{', ']':'[', ')':'('} # we can only use key to find value, can't reverse
        for i in s:
            if i in ref.values():
                stack.extend(i)
            elif i in ref.keys():
                if stack == [] or ref[i] != stack.pop():
                    return False
            else:
                return False

        return stack == []