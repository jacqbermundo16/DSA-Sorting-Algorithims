# reference - https://www.youtube.com/watch?v=5KjapFQNxUo

def sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j
                
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


nums = [39, 77, 46, 23, 94, 3, 98, 19, 62, 2]
sort(nums)
print(nums)