class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        # Count the element frequencies
        for n in nums:
            freq_map[n] = freq_map.get(n,0) + 1
        
        # Use Bucket Array - Collect same frequency elements in the same index
        buckets = [[] for i in range(len(nums)+1)]
        for value,freq in freq_map.items():
            buckets[freq].append(value)
        
        # Extract the top K elements
        top_k = []
        for i in range(len(nums),0,-1):
            top_k.extend(buckets[i])
            if len(top_k) == k:
                return top_k

        
