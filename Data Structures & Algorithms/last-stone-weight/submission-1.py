class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [stone * -1  for stone in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            s1 = heapq.heappop(self.stones)
            s2 = heapq.heappop(self.stones)
            if s2 > s1:
                heapq.heappush(self.stones, s1 - s2)
        self.stones.append(0)
        return abs(self.stones[0])