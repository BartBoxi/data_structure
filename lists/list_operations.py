if __name__ == '__main__':
    N = int(input())
    lista = []
    for i in range(N):
        comand = (input()).split()
        if comand[0] == 'print':
            print(lista)
        elif comand[0] == 'insert':
            lista.insert(int(comand[1]), int(comand[2]))
        elif comand[0] == 'append':
            lista.append(int(comand[1]))
        elif comand[0] == 'remove':
            lista.remove(int(comand[1]))
        elif comand[0] == 'sort':
            lista.sort()
        elif comand[0] == 'pop':
            lista.pop()
        elif comand[0] == 'reverse':
            lista.reverse()