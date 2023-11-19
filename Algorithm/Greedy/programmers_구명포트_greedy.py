from collections import deque
def solution(people, limit):
    answer = 0    
    people.sort()
    result = list()
    boat = list()
    queue = deque(people)
    while queue:
        if len(queue) == 1:
            answer += 1 
            break
        if queue[0] + queue[-1] <= limit:
            queue.popleft()
            queue.pop()
        else:
            queue.pop()
        answer += 1
    return answer

print(solution([70, 80, 50, 50], 100))
