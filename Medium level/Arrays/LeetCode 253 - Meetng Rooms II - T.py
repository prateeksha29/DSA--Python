"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""

# Two pointers
# split and sort the start and end times
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        start_p = 0
        end_p = 0
        rooms = 0

        while start_p < len(intervals):
            if start[start_p] < end[end_p]:
                rooms += 1
                start_p += 1
            else:
                start_p += 1
                end_p += 1

        return rooms



# Priority queues or min heap data structure
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)
