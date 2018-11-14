'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # this function sucks man!
        res = [0] * 32
        for i in range(31, -1, -1):
            res[i] = (n // (2 ** i))
            n -= (2 ** i) * res[i]

        return sum(res)

        # # we could use build in bits function
        # return bin(n).count('1')