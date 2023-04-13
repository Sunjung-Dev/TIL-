def solution(sizes):
    answer = 0

    w = []
    h = []

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])

        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])
    answer = max(w) * max(h)
    return answer

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))