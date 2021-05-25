class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Set up pointers for each colour / number (red = 0, white = 1 and blue = 2)
        red, white, blue = 0, 0, len(nums) - 1
        
        # Loop until white pointer passes blue 
        while white <= blue:

            # if the value at the white 0 we swap it with the red index and increment the red index 
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            
            # if the value at the white 1 we simply increment (its in the right place) 
            elif nums[white] == 1:
                white += 1

            # if the value at white is 2 we swap with blue and decrement the blue index
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1