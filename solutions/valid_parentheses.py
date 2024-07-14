class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False

        left_brackets = []

        bracket_map = {"}": "{", "]": "[", ")": "("}

        for c in s:
            if c in ["(", "{", "["]:
                left_brackets.append(c)
            else:
                left_bracket = left_brackets.pop() if left_brackets else None
                if left_bracket != bracket_map.get(c):
                    return False

        if len(left_brackets) > 0:
            return False


class TestCase:
    def __init__(self, input: str, expectedOutput: bool):
        self.input = input
        self.expectedOutput = expectedOutput
        self.actualOutput = Solution().isValid(input)

    def __repr__(self):
        return f"s: {self.input} => expectedOutput: {self.expectedOutput}, actualOutput: {self.actualOutput}"


testCases = [
    TestCase("()", True),
    TestCase("()[]{}", True),
    TestCase("(]", False),
    TestCase("([)]", False),
    TestCase("{[]}", True),
]

for t in testCases:
    print(t)
    assert t.actualOutput == t.expectedOutput
