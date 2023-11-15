from collections import deque 
def bfs(start_node, final_node):
    need_visited = deque()
    need_visited.append(start_node)
    sec, cnt = 0, 0
    node_cnt = 0

    while need_visited:
        node = need_visited.popleft()
        for next_node in [node-1, node+1, node*2]:
            node_cnt += 1
            print(node_cnt)
            if next_node == K:
                cnt += 1
            else:
                need_visited.append(next_node)
        print(need_visited)
        sec += 1
        if sec == 4:
            print(cnt)
            break
    


N, K = map(int, input().split())
print(bfs(N, K))