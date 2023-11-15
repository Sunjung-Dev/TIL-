def solution(brown, yellow):
    answer = []
    total_carpet = brown + yellow
    for i in range(1, total_carpet+1):
        if total_carpet % i == 0:
            if ((i-2) * (int(total_carpet/i)-2)) == yellow:
                answer.append(int(total_carpet/i))
                answer.append(i)
                return answer

print(solution(10, 2))