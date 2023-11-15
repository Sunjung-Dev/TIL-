from collections import deque

N, M = map(int, input().split())
graph = list()

visited = [0 for i in range(N)]

def bfs(node):
    queue = deque()
    queue.append(node)

    while(queue):
        node = queue.popleft()
        for i in range(len(graph)):
            if not visited[i]:
                visited[i] = visited[node] + 1
                queue.append(i)

for i in range(N):
    a, b = map(int, input().split())
    graph.append((a, b))
    
res = list()

for i in range(N):
    if visited[graph[i][0]] == 0:
        visited[graph[i][0]] = 1
        bfs(graph[i][0])
        res.append(sum(visited))
print(res.index(min(res))+1)