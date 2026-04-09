class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Get the unique values from the list
        num_set = set(nums)
        longest_seq = 0

        for n in nums:
            # Check for a potential start of a sequence (number should be the first in the sequence)
            if n-1 not in num_set:
                length = 0
                
                next_n = n
                while next_n in nums:
                    length += 1
                    next_n += 1
                longest_seq = max(longest_seq,length)

        return longest_seq 