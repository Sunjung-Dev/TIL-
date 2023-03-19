def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0, target, answer, 0)
    return answer

# dfs 방식으로 접근
def dfs(numbers, i, target, answer, value):

    #재귀함수 사용

    if i == len(numbers) and target == value:
        answer += 1
        return 

    if i == len(numbers):
        return

    dfs(numbers, i+1, target, answer, value + numbers[i])
    dfs(numbers, i+1, target, answer, value - numbers[i])    
    
    return answer

print(solution([1, 1, 1, 1, 1], 3))