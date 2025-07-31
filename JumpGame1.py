class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target = len(nums) -1
        for i in range(target-1,-1,-1):
           if target - i <= nums[i]:
            target = i
                
        return (target == 0)


##Original Bad Solution
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         target = len(nums) -1
#         possible = []

#         possible.append(target)
#         for i in range(target-1,-1,-1):
#             print(i)
#             for j in range(len(possible)):
#                 if possible[j] - i <= nums[i]:
#                     possible.append(i)
#                     break
                
            

#         return (0 in possible)
