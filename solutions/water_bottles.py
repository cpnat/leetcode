# https://leetcode.com/problems/water-bottles/


class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        drank, filled_bottles, total_bottles = 0, numBottles, numBottles

        while total_bottles >= numExchange:
            drank += filled_bottles

            filled_bottles = total_bottles // numExchange
            total_bottles = filled_bottles + (total_bottles % numExchange)

        drank += filled_bottles

        return drank


class TestCase:
    def __init__(self, numBottles: int, numExchange: int, expectedOutput: int):
        self.numBottles = numBottles
        self.numExchange = numExchange
        self.expectedOutput = expectedOutput
        self.actualOutput = Solution().numWaterBottles(numBottles, numExchange)

    def __repr__(self):
        return f"numBottles: {self.numBottles}, numExchange: {self.numExchange} => expectedOutput: {self.expectedOutput}, actualOutput: {self.actualOutput}"


testCases = [TestCase(9, 3, 13), TestCase(15, 4, 19)]

for t in testCases:
    print(t)
    assert t.actualOutput == t.expectedOutput
