'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = []
        for i in range(numRows):
            tmp = [1] * (i + 1)
            for j in range(1, i):
                tmp[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(tmp)

        return res