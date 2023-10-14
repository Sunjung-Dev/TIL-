def solution(name):
    answer = 0
    
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(0, len(name)):
        if i == len(name) - 1 :
            pass
        else:
            idx = alphabet_list.index(name[i])
            next_idx = alphabet_list.index(name[i+1])
            print(idx, next_idx)
            if idx == 0 or idx == len(name):
                result = idx + 1 + ( 26 - next_idx)
                print(result)
                if result < next_idx - idx:
                    answer += result
                else:
                    answer += next_idx 

            if next_idx == 0 or next_idx == len(name):
                result = idx + 1 + ( 26 - next_idx)
                print(result)
                if result < idx - next_idx:
                    answer += result
                else:
                    answer += idx

            # else:
            #     answer += abs(idx-next_idx)
            # answer += (idx + next_idx)
    print(answer)
    return answer

solution("jan")
