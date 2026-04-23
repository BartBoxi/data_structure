def increasingTriplet(nums:List[int]) -> bool:
    
    # brute force 
    
    first = (float('inf'))
    second = (float('inf'))
    
    for i in range(len(nums)):
        if nums[i] <= first:
            first = nums[i]
        elif nums[i] > first and nums[i] <= second:
            second = nums[i]
        elif nums[i] < second:
            third = nums[i]
            return True
    else:
        return False
    
    
    
    
    
print(increasingTriplet(nums = [5,4,3,2,1]))