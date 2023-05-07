from collections import deque


def bfs(start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()
        visited.append(node)
        if node - 1 not in visited:
            need_visited.append(node-1)
        if node + 1 not in visited:
            need_visited.append(node+1)
        if node * 2 not in visited:
            need_visited.append(node*2)

    print(need_visited)
    return need_visited

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(bfs(5))



