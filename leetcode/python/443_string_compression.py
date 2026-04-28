



    
#     s = ""
    
#     seen = {}

#     for i in chars:
#         if i not in seen:
#             seen[i] = 1
#         else:
#             seen[i] += 1
    
#     s = "".join(f"{key}{value}" for key, value in seen.items())
#     wynik = [str(element) for para in seen.items() for element in para]
    
#     return len(wynik)

# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]



    ## check if there is just one element in the input list of string 

###
#MOJE ROZWIAZANIE ALE NIE IN PLACE 
###
### moje rozwiazanie jest ok, ale to nie jest edycja wejsciowej listy in place! 

# def compress(chars) -> int:
    
#     s = ""

#     seen = {}

#     for i in chars:
#         if i not in seen:
#             seen[i] = 1
#         else:
#             seen[i] += 1
    
#     print(seen)
    
#     for key,value in seen.items():
#         if value == 1:
#             s += key
#         else:
#             s += f"{key}{value}"
#     return len(s)

# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c"]

# print(compress(chars))

###

### Poprawne rozwiazanie aby spelnilo to wymagania z leetcode 

def compress(chars) -> int:
    # 1. Tworzymy Twój wynikowy string 's' (używając Twojej logiki)
    seen = {}
    for i in chars:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1
    
    s = ""
    for key, value in seen.items():
        if value == 1:
            s += key
        else:
            s += f"{key}{value}"
    
    # 2. KLUCZOWY MOMENT: Musisz zmodyfikować listę chars!
    # Czyścimy starą listę i wstawiamy do niej znaki z napisu 's'
    for i in range(len(s)):
        if i < len(chars):
            chars[i] = s[i]
        else:
            chars.append(s[i])
            
    # Usuwamy nadmiarowe elementy, jeśli nowa lista jest krótsza niż stara
    del chars[len(s):]

    return len(s)




