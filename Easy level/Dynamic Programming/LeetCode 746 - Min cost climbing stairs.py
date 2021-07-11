"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next_1 = cost[len(cost) - 2]
        next_2 = cost[len(cost) - 1]
        for i in range(len(cost) - 3, -1, -1):
            f = cost[i] + min(next_1, next_2)
            next_1, next_2 = f, next_1
        return min(next_1, next_2)
