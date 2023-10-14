import itertools
import sys

N, M, K = map(int, input().split())
box_weight = list(map(int, input().split()))

box_lists = itertools.permutations(box_weight, N)

#box_list => 입력 받은 값들이 Permutation된 값들 리스트로 있을 것
for box_list in box_lists:

    box_list = list(box_list)

    total_box_weight = 0 #총 무게 
    rail_weight = 0 #한번 레일에 올려놓을 무게 
    i = 0
    work = 0

    # K횟수 만큼 돌려야 됨 
    while work != K:
        if box_list[i] + rail_weight <= M:
            rail_weight += box_list[i]
            # box_list.append(box_list[i])
            i += 1

        else:
            total_box_weight += rail_weight
            rail_weight = 0
            work += 1

    result = min(result, total_box_weight)

print(total_box_weight)


from itertools import permutations
import sys
input = sys.stdin.readline 

n, m , k = map(int,input().split())
input_rails = list(map(int,input().split()))

rails_info = permutations(input_rails, n)

result = sys.maxsize

for now_rails in rails_info:

    rails = list(now_rails)

    i = 0
    bucket = 0
    work = 0
    this_all = 0
    
    while work != k: # 작업의 수만큼만 반복
        if bucket + rails[i] <= m:  #m: 바구니 무게
            bucket += rails[i]
            rails.append(rails[i])
            i+=1
        else: 
            this_all += bucket
            bucket = 0
            work += 1
            
    result = min(result, this_all)

print(result)