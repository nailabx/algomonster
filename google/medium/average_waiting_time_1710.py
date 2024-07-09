from typing import List

class AverageWaitingTime:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_times:int = 0
        available_time: int = 0
        for arrival, t in customers:
            available_time = max(available_time, arrival) + t
            total_times += available_time - arrival
        return total_times/len(customers)


