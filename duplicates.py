class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Cyclic sort: Place each number at its correct index (number n goes to index n-1)
        for i in range(len(nums)):
            # Keep swapping current element to its correct position
            # until current position has the right element or a duplicate
            while nums[i] != nums[nums[i] - 1]:
                # Get the correct index for current element
                correct_index = nums[i] - 1
                # Swap current element with element at its correct position
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
      
        # After cyclic sort, elements not at their correct position are duplicates
        # Element at index i should be i+1 if no duplicates
        duplicates = []
        for index, value in enumerate(nums):
            if value != index + 1:
                duplicates.append(value)
      
        return duplicates