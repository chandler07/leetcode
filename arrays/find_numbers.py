from typing import List

class Solution:

    def getNumOfDigits(self, num: int) -> int:
        return len(str(num))


    def isEvenNumOfDigits(self, num: int) -> int:
        size = self.getNumOfDigits(num)
        return size % 2 == 0 

    def findNumbers(self, nums: List[int]) -> int:
        count_evens = 0

        for num in nums:
            if self.isEvenNumOfDigits(num):
                count_evens += 1
        return count_evens


    
