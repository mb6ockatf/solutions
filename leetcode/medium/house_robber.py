#!/usr/bin/env python3
# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = nums + [0]
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        return nums[0]
