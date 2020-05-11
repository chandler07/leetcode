from typing import List

class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:

        for i in range(0, len(arr)):
            if arr[i] == 0:
                print(arr[i+1])
                arr[i+1] = 0
            print(arr)
sol = Solution()
sol.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
