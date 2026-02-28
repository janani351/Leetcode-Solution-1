class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Initialize result array with -1 (no greater element found)
        stack = []  # Monotonic decreasing stack to track potential next greater elements
      
        # Iterate through the circular array twice (simulate circular by going 2*n times)
        # Process from right to left to build next greater elements
        for i in range(n * 2 - 1, -1, -1):
            index = i % n  # Get actual index in the original array (circular indexing)
          
            # Pop elements from stack that are less than or equal to current element
            # These cannot be the next greater element for current position
            while stack and stack[-1] <= nums[index]:
                stack.pop()
          
            # If stack is not empty, top element is the next greater element
            if stack:
                result[index] = stack[-1]
          
            # Push current element to stack for future comparisons
            stack.append(nums[index])
      
        return result