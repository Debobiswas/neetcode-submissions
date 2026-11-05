class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i,n in enumerate(nums):
            if n not in counter:
                counter[n] = 1
            else:
                counter[n]+=1

   
        sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        ret = []
        
        for i in range(k):
            ret.append( sorted_items[i][0])
        
        return ret