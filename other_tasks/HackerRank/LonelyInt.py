a = [1,2,3,4,3,2,1]


def lonelyinteger(a):
    sum_of_array = sum(set(a))
    print(sum_of_array)
    sum_of_a = sum(a)
    return sum_of_array * 2 - sum_of_a



