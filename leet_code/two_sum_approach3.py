#!/usr/bin/env python

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i
        raise ValueError("No two sum solution")


if __name__ == '__main__':
    assert [0, 1] == Solution().twoSum([2, 7, 11, 15], 9)
    assert [1, 2] == Solution().twoSum([2, 5, 5, 11], 10)
