def min_value(nums1:list[int], nums2:list[int]):
    i = 0
    j = 0

    common_element = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            common_element.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j +=1
    return min(common_element)





### testing part
nums1 = [1,2,3]
nums2 = [2,4]

print(min_value(nums1, nums2))

