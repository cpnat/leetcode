class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        str_x = str(x)

        start, end = 0, len(str_x) - 1

        while start <= end:
            if str_x[start] != str_x[end]:
                return False
            start += 1
            end -= 1

        return True


class TestCase:
    def __init__(self, x: int, expectedOutput: bool):
        self.x = x
        self.expectedOutput = expectedOutput
        self.actualOutput = Solution().isPalindrome(x)

    def __repr__(self):
        return f"x: {self.x} => expectedOutput: {self.expectedOutput}, actualOutput: {self.actualOutput}"


test_cases = [TestCase(121, True), TestCase(-121, False), TestCase(10, False)]

for t in test_cases:
    print(t)
    assert t.expectedOutput == t.actualOutput
