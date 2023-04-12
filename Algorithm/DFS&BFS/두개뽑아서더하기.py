def dfs(numbers, i, root_node, answer):
    for j in range(len(numbers)):
        if i == j:
            continue
        answer.append(root_node + numbers[j])
        i += 1
    if i < len(numbers):
        dfs(numbers, i, numbers[i], answer)

def solution(numbers):
    answer = []
    dfs(numbers, 0, numbers[0], answer)
    return sorted(list(set(answer)))

print(solution([5,0,2,7]))