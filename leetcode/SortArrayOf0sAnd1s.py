from typing import List

def sortArray(nums: List[int]) -> None:
    zero, one = 0, len(nums) - 1

    while zero <= one:
        if nums[zero] > nums[one]: 
            nums[zero], nums[one] = nums[one], nums[zero]
        if nums[zero] == 0: zero += 1
        if nums[one] == 1: one -= 1

def main():
    array = [1,0,0,1,0,1]
    array1 = [1]
    array2 = [0,0,0]
    array3 = [0,1,0]
    sortArray(array)
    sortArray(array1)
    sortArray(array2)
    sortArray(array3)
    print(array)
    print(array1)
    print(array2)
    print(array3)

if __name__ == "__main__":
    main()