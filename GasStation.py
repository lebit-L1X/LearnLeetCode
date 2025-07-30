'''You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [gas[x] - cost[x] for x in range (len(cost))]
        total = 0
        debt = 0
        startingpoint = -1
        feasible = False
        print(net)
        for i in range(len(cost)):
            if (not feasible):
                startingpoint = i
            total += net[i]
            feasible = True
            if (total < 0):
                debt += total
                total = 0
                feasible = False
                pass
            print(f"feasible:{feasible} {i}")
            print(f"total:{total}")
            print(f"debt:{debt}")
        
        if total + debt >= 0:
            return startingpoint
        return -1
                
            
            