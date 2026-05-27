"""
U: 
    input: int array "heights" 
    output: the max amount of water a container can store 
    
    choose 2 bars to form a container 
Match: 2 ptr, area = (right - left) * min(left,right)
Plan: 
    max_area = 0
    1. 2 ptr, left = 0, right = len(height) - 1
    2. while left < right
        3. width = right - left 
        4. hgt = min(height[left], height[right])
        5. area = width * hgt
        if area > max_area, update max area

        if left < right:
            left += 1 
        else:
            right -= 1
    6. return max_area
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while (left < right):
            width = right - left
            hgt = min(height[left],height[right])
            area = width * hgt

            if area > max_area:
                max_area = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        