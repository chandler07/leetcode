from typing import List

class Solution:

    def squareNum(self, num: int) -> int:
        return num*num

    def sortedSquares(self, A: List[int]) -> List[int]: 
        tmp_ary = []
        for num in A:
            tmp_ary.append(self.squareNum(num))
        tmp_ary.sort()
        return tmp_ary
