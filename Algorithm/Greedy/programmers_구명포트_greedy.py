def solution(people, limit):
    answer = 0    
    cnt = 0 
    people.sort()
    boat = list()
    result = list()
    # for per in people:
    #     print(per)
    #     if (per < limit) and (sum(boat) + per <= limit):
    #         boat.append(per)
    #     else:
    #         boat = list()
    #         boat.append(per)
    #     result.append(boat)
    # print(result)

    for i in range(len(people)-1, -1, -1):
        if (people[i] < limit) and (sum(boat) + people[i] <= limit):
            boat.append(people[i])
            print("1", boat)
        else:
            boat = list()
            boat.append(people[i])
            print("2", boat)
            continue
        result.append(boat)
        # result.append(boat)
    print(result)
    return answer

solution([70, 50, 80, 50], 100)
