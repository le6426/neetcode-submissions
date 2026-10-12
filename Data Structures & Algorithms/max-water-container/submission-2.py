class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(heights) - 1
        maximum = 0

        while leftPointer < rightPointer:
            
            if heights[leftPointer] < heights[rightPointer]:
                area = heights[leftPointer] * (rightPointer - leftPointer)
                leftPointer += 1
            else:
                area = heights[rightPointer] * (rightPointer - leftPointer)
                rightPointer -= 1

            maximum = max(area, maximum)

        return maximum