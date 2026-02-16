# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(nums: list[int], n: int) -> list[int]:
    left_array = []
    right_array = []
    new_array = []
    for i in range(n):
        left_array.append(nums[i])
    for j in range(n, 2*n):
        right_array.append(nums[j])
    
    print(left_array)
    print(right_array)

    for k in range(0,n):
        new_array.append(left_array[k])
        new_array.append(right_array[k])
    return new_array

### faster solution 

def shuffle2(nums: list[int], n: int) -> list[int]:
    new_array = []
    for i in range(n):
        new_array.append(nums[i])
        new_array.append(nums[i + n])
    return new_array



nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))
print(shuffle2(nums, n))
