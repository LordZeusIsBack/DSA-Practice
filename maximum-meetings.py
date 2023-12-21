from typing import List, Tuple

class Solution:
    def maxMeetings(self, N: int, S: List[int], F: List[int]) -> List[int]:
        meetings = [(S[i], F[i], i+1) for i in range(N)]
        meetings.sort(key=lambda x: x[1])
        result = []
        end_time = 0
        for meeting in meetings:
            start_time, finish_time, meeting_index = meeting
            
            if start_time > end_time:
                result.append(meeting_index)
                end_time = finish_time
        result.sort()
        return result

# https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1