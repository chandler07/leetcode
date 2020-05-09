class Solution:
   
    def twoSum(self, nums, target):
        two_sum_list = []
        for idx, num in enumerate(nums):
            print("Iteration #: ", idx)
            if target - num == nums[idx -1]:
                print("Found it")
                two_sum_list.extend((idx-1, idx))
                print(two_sum_list)
                return two_sum_list

sol = Solution()
#sol.twoSum(nums = [2, 7, 11, 15], target = 9)