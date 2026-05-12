class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        max_left = height[0]
        max_right = height[len(height)-1]
        l = 0
        r = len(height)-1
        water = 0

        while l < r:

            if height[l] <= height[r]:
                if max_left-height[l] > 0:
                    water += max_left-height[l]
                l+=1
            else:
                if max_right-height[r] > 0:
                    water += max_right-height[r]
                r-=1
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])


        return water
            








