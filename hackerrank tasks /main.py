import re

# def camelcase(word):


def process():
    pattern = "r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])'"

    s = "S;M;plasticCup()"
    s = s.split(";")
    if s[0] == "S":
        new_word = re.findall(pattern, s[2])
        new_word = [word.lower() for word in new_word]
        result = ''.join(new_word)
        print(result)

process()