### if you got a string even indexed and odd indexed
### characters, separate them and print as a single
### string but separated e.g. abcdef abc def

T = int(input()) ### as first we are getting int saying how
### many iterations are needed and how many inputs we got

for _ in range(T):
    S = str(input())


    odd = ""
    even = ""

    for i,c in enumerate(S):
        if i%2 == 0:
            even += c
        else:
            odd += c

    print(even, odd)
