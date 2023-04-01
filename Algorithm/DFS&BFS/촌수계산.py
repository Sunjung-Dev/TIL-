def dfs(relation_list, root_node, visited=[], result=0):
    if root_node not in visited:
        print("yes", root_node)
        result += 1
        visited.append(root_node)
    for i in range(len(relation_list)):
        if relation_list[i][0] == root_node:
            if relation_list[i][1] not in visited:
                dfs(relation_list, relation_list[i][1], visited, result)
    print("kkk")
    print(result)
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
 
    result_list = dfs(relation_list, relation_list[0][0])
    
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