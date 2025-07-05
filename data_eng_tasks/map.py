names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

names_map = map(str.upper, names)

print(type(names_map))
print(names_map)


names_uppercase = [*names_map]
print(names_uppercase)

