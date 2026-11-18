class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minh = []
        m = {}
        final = []
        for n in nums:
            if n in m:
                m[n] += 1
            else: 
                m[n] = 1
            

        for key,value in m.items():
            heapq.heappush(minh,(value,key))
            
            if len(minh) > k:
                heapq.heappop(minh)
        while minh:
            value = heapq.heappop(minh)

            final.append(value[1])
        return final


