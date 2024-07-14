# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_map = {v: i for i, v in enumerate(nums)}

        for i in range(len(nums)):
            remainder = target - nums[i]
            matched_num = nums_map.get(remainder, None)

            if matched_num and matched_num != i:
                return [min(i, matched_num), max(i, matched_num)]


class TestCase:
    def __init__(self, nums: list[int], target: int, expected_output: list[int]):
        self.nums = nums
        self.target = target
        self.expected_output = expected_output
        self.actual_output = Solution().twoSum(nums, target)

    def __repr__(self):
        return f"nums: {self.nums}, target: {self.target} => expectedOutput: {self.expected_output}, actualOutput: {self.actual_output}"


test_cases = [
    TestCase([2, 7, 11, 15], 9, [0, 1]),
    TestCase([3, 2, 4], 6, [1, 2]),
    TestCase([3, 3], 6, [0, 1]),
]

for t in test_cases:
    print(t)
    assert t.actual_output == t.expected_output
