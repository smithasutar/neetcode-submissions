class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_height = 0
        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                l = min(heights[j], heights[i])
                area = l*(j-i)
                largest_height = max(area, largest_height)

        return largest_height


        