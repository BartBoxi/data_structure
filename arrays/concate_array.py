# concat the array with itself 
#Build an array of size 2 * n and assign num[i] to ans[i] and ans[i + n]

def getConcatenation(nums: List[int]) -> List[int]:
    new_array = []
    for i in range(2): ### tutaj idziemy ile razy ma ta pierwsza tablica przejsc 
        for j in nums:
            new_array.append(j) ### tu dodajemy do nowej tablicy elementy z pierwszej tablicy 
    return new_array


print(getConcatenation([1,2,3,4,5]))