graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}


seen = set()


def dfs(start):
    stack = [start]

    seen.add(start)
    print(f"Starting DFS at : {start}")

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in seen:
                print(f"Found unvisited neighbor: {neighbor}")
                seen.add(neighbor)
                stack.append(neighbor)
                print(f"    Added {neighbor} to 'seen'. Seen is now: {seen}")
                print(f"    Pushed {neighbor} to stack. Stack is now: {stack}")
            else:
                print(f" Found visited neighbor: {neighbor}. Skipping")
    print("DFS complete. Stack is empty")


print(dfs('A'))





