class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_inx,r_inx = 0,len(heights)-1
        max_area = 0

        while l_inx < r_inx:

            # Calculate current area: least wall height(l and r) * distance between l and r
            container_area = min(heights[l_inx],heights[r_inx]) * (r_inx-l_inx)
            if container_area > max_area:
                max_area = container_area
            
            # Move the walls (Preference to max height)
            if heights[r_inx] >= heights[l_inx]:
                l_inx +=1
            else:
                r_inx -=1

        return max_area
