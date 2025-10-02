from collections import defaultdict


def KeysandRooms(rooms):

    visited = {0}
    to_do = [0]

    while to_do:
        current_room = to_do.pop()
        for key in rooms[current_room]:
            if key not in visited:
                visited.add(key)
                to_do.append(key)
    return len(visited) == len(rooms)


rooms = [[1],[2],[3],[]]

print(KeysandRooms(rooms))


