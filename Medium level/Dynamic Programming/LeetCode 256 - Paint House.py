"""

"""
# Recursion with memoization
class Solution:
    def paint_cost(self, costs, n, color):
        if (n, color) in self.memo:
            return self.memo[(n, color)]
        total_cost = costs[n][color]
        if n == len(costs) - 1:
            pass
        elif color == 0:
            total_cost += min(self.paint_cost(costs, n + 1, 1), self.paint_cost(costs, n + 1, 2))
        elif color == 1:
            total_cost += min(self.paint_cost(costs, n + 1, 0), self.paint_cost(costs, n + 1, 2))
        else:
            total_cost += min(self.paint_cost(costs, n + 1, 0), self.paint_cost(costs, n + 1, 1))

        self.memo[(n, color)] = total_cost
        return total_cost

    def minCost(self, costs: List[List[int]]) -> int:
        self.memo = {}
        result = [self.paint_cost(costs, 0, paint) for paint in range(len(costs[0]))]

        return min(result)




# Dynamic Programming
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for house in range(len(costs)-2, -1, -1):
            costs[house][0] += min(costs[house+1][1], costs[house+1][2])
            costs[house][1] += min(costs[house+1][0], costs[house+1][2])
            costs[house][2] += min(costs[house+1][0], costs[house+1][1])
        return min(costs[0])


# DP without overwriting the original array
import copy

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        if len(costs) == 0: return 0

        previous_row = costs[-1]
        for n in reversed(range(len(costs) - 1)):

            current_row = copy.deepcopy(costs[n])
            # Total cost of painting nth house red?
            current_row[0] += min(previous_row[1], previous_row[2])
            # Total cost of painting nth house green?
            current_row[1] += min(previous_row[0], previous_row[2])
            # Total cost of painting nth house blue?
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row

        return min(previous_row)
