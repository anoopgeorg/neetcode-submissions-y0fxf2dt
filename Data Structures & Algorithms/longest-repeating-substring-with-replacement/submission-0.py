class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_len = 0
        max_f = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            max_f = max(max_f,count[s[r]])
            if (r-l+1) - max_f > k:
                count[s[l]] -= 1
                l += 1

            window_size = r-l+1
            max_len = max(max_len,r-l+1)
        
        return max_len