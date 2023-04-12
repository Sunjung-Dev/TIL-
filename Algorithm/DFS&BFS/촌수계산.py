def dfs(relation_list, target_1, target_2, visited=[]):
    visited.append(root_node)

    for i in range(len(relation_list)):
        if relation_list[i][0] == root_node: 
            if relation_list[i][1] not in visited:
                dfs(relation_list, target_1, target_2, visited)
                
    return visited



def input_n_answer():
    relation_list = list()

    # 전체 사람의 수 
    n = int(input())

    #촌수를 계산해야하는 서로 다른 두 사람의 번호 
    target_1, target_2 = map(int, input().split())

    # 부모 자식들 간의 관계의 개수 m
    m = int(input())

    for i in range(m):
        parent, kid = map(int, input().split())
        relation_list.append([parent, kid])
 
    result_list = dfs(relation_list, target_1, target_2)

    
    if target_1 not in result_list or target_2 not in result_list:
        return -1
    else:
        return abs(result_list.index(target_1) - result_list.index(target_2))

    
print(input_n_answer())

# 반례 1 
# 4
# 1 4
# 3
# 1 2
# 2 3
# 2 4



# def dfs(v,cnt):
#   cnt += 1
#   visited[v] = True
#   # 찾아야 하는 사람의 번호를 방문했을 때
#   if v == b:
#     result.append(cnt)
#   for i in graph[v]:
#     if not visited[i]:
#       dfs(i,cnt)







# def make_set(n):
#     root = [element for element in range(1,n+1)]
#     return root
    
# def union(x,y):
#   if  x < y:
#     root[y-1]=x
#   else:
#     root[x-1]=y

# def parent(x):
#   return root[x-1]

# def count_root(x, y, count):
#     while True:
#         if x>y and parent(x) != x:
#             x = parent(x)
#             count += 1
#         elif x<y and parent(y) != y:
#             y = parent(y)
#             count += 1
#         else:
#             break
    
#     if parent(x) != parent(y):
#         return -1
#     else:
#         return count


# n=int(input()) #Node
# query1, query2 = map(int, input().split()) #Query

# e=int(input()) #Edges

# root=make_set(n)


# for i in range(e):
#     alpha, beta =map(int,input().split())
#     union(alpha, beta)
    

# print( count_root(query1, query2, 0) )


#반례
#4 
#4 2 
#3 
#2 3
#3 1
#3 4