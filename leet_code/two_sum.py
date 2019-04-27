#!/usr/bin/env python3


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[(i+1):]):
                if target == num1 + num2:
                    return [i, (i+1)+j]
        return []


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)
    assert [0, 1] == result
