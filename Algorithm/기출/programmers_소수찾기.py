def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.split("},")
    s[-1] = s[-1].replace('}', '')
    s.sort(key=len)
    for i in range(len(s)):
        if i == 0:
            answer.append(int(s[i]))
        else:
            s[i] = s[i].split(",")
            for j in range(len(s[i])):
                if int(s[i][j]) == answer[0]:
                    pass
                elif int(s[i][j]) not in answer:
                    answer.append(int(s[i][j]))
    return answer

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")