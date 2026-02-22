class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # HashMap to store the first occurrence index of each cumulative sum
        # Initialize with sum 0 at index -1 (before array starts)
        sum_to_index = {0: -1}
      
        # Track maximum length and running cumulative sum
        max_length = 0
        cumulative_sum = 0
      
        # Iterate through the array with index and value
        for index, value in enumerate(nums):
            # Treat 1 as +1 and 0 as -1 for cumulative sum
            # This way, equal numbers of 0s and 1s will have sum = 0
            cumulative_sum += 1 if value == 1 else -1
          
            # If we've seen this sum before, we found a subarray with equal 0s and 1s
            if cumulative_sum in sum_to_index:
                # Calculate length from first occurrence to current index
                current_length = index - sum_to_index[cumulative_sum]
                max_length = max(max_length, current_length)
            else:
                # First time seeing this sum, record its index
                sum_to_index[cumulative_sum] = index
      
        return max_length