#Given a list of integers, count and return the number of times each value appears as
# an array of integers.

def countingSort(arr):
    result = [0] * 100 # the n so len of the arr
    for i in range(len(arr)):
        result[arr[i]] +=1
    return result


arr = [0,1,2,3]
print(countingSort(arr))

