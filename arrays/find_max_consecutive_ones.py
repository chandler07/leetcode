from typing import List

class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        tmp_max = 0

        for num in nums:

            if num == 0:
                tmp_max = 0
            if num == 1:
                tmp_max +=1
                if tmp_max > max_consecutive:
                    max_consecutive = tmp_max
        return max_consecutive