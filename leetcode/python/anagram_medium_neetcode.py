# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     posortowane = {}
#     for string in strs:
#         klucz = "".join(sorted(string))
#         print(klucz)
#         if klucz in posortowane:
#             posortowane[klucz].append(string)
#         else:
#             posortowane[klucz] = [string]
#     return list(posortowane.values())
            





# strs = ["act","pots","tops","cat","stop","hat"]

# print(groupAnagrams(strs))


def joining(strs:list[str]):
    for string in strs:
        #klucz = "".join(sorted(string))
        print(string)


strs = ["act","pots","tops","cat","stop","hat"]

print(joining(strs))