def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
            print(nums)

nums = [39, 77, 46, 23, 94, 3, 98, 19, 62, 2]
sort(nums)

print(nums)