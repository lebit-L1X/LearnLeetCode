class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = nums.copy()
        nums.sort()
        i = 0
        j = len(nums) - 1


        for _ in range(len(nums)):
            if nums[i] + nums[j] == target:
                break
            elif nums[i] + nums[j] < target:
                i+= 1
            elif nums[i] + nums[j] > target:
                j-= 1
        ansa=[]
        for x in range (len(nums2)):
            if nums2[x] == nums[i]:
                ansa.append(x)
            elif nums2[x] == nums[j]:
                ansa.append(x)
        return ansa


        