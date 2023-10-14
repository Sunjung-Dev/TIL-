from collections import deque


def bfs(start_node, final_node):
    visited = list()
    need_visited = deque()
    need_visited.append(start_node)
    cnt = 0 
    answer = 0
    sec = 0 

    while need_visited:
        node = need_visited.popleft()
        if node >= 100:
            break

        if node not in visited:
            visited.append(node)
        
            for next_node in [node-1, node+1, node*2]:
                if next_node == final_node:
                    cnt += 1

                if next_node not in visited:
                    need_visited.append(next_node)

            sec += 1
    return cnt

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(bfs(N, K))


#준용님 코드 
# from collections import deque

# a,b = map(int,input().split())  #수빈이가 있는 위치와 동생이 있는 위치 입력
# que = deque()
# que.append([a])
# cnt = 0
# visited = {5:0}
# check = []

# if a == b:
#     print(0)
#     print(0)

# else:
#     while que:
    
#         add = []
#         current = que.popleft()
#         if b in current:
#             break 
#         for j in current:
#             child = [j-1,j+1,j*2]
#             for k in child:
#                 if k < 0 or k > 100000:
#                     continue 
#                 if not visited.get(k):
#                     visited[k] = 1 
#                     add.append(k)
#                 else:
#                     visited[k] += 1 
#         que.append(add)
#         cnt += 1

#     print(cnt)
#     print(visited[b])