lista = [" google ", "YouTube", " ALPHABET ", "Google"]


# def clean_list(list):
#     for i in lista:
#         print(i.strip().lower())



# print(clean_list(lista))


# how to do it with set comprehension

print({i.strip().lower() for i in lista})