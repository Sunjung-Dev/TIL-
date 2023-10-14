from collections import deque


def bfs(start_node, final_node):
    visited = list()
    need_visited = deque()
    need_visited.append(start_node)
    cnt = 0 
    answer = 0

    while need_visited:
        node = need_visited.popleft()
        visited.append(node)

        if len(need_visited) >= 100000:
            break
       
        for next_node in [node-1, node+1, node*2]:
            if next_node == final_node:
                cnt += 1

            if next_node not in visited:
                need_visited.append(next_node)
        
    print(answer)
    return cnt

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(bfs(N, K))