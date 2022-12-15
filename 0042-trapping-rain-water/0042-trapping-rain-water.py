class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        output = 0
        stack = []
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - height[top]
                w = i - stack[-1] - 1
                output += h * w
            stack.append(i)
        return output