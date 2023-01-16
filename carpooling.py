class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        passangers = [0]*1001
        # lazy propagation
        for count, fr, to in trips:
            if count > capacity: return False  # optimization 1
            passangers[fr] += count
            passangers[to] -= count
        # calculate now the exact passanger counts and see if we exceed capacity
        for i in range(1, len(passangers)):
            passangers[i] += passangers[i-1]
            if passangers[i] > capacity:
                return False
        return True