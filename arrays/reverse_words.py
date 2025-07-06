s = "Let's take LeetCode contest"

def reverse(s:str):
    new_list = []
    lista = s.split(" ")
    for i in lista:
        new_list.append(i[::-1])
    return " ".join(new_list) 


print(reverse(s))