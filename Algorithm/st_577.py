from collections import deque

#시작점 찾기 
def check(x, y):
    pass


def bfs(map_info):
    queue = deque()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue.append([map_info[0][0], map_info[0][1]])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #본인 위치를 기준으로 
            if i == 0: #한칸 밑으로 
                if nx == 0 or 
                pass
            if i == 1: #한칸 위로 
                pass  
            if i == 2: #한칸 왼쪽으로 
                 pass
            if i == 3: #한칸 오른쪽으로 
                pass




    # return 


def main():
    H, W = map(int, input().split())
    map_info = list()
    for i in range(H):
        road = list(map(str, input()))
        map_info.append(road)

    for i in range(len(map_info)):
        for j in range(len(map_info[i])):
            if map_info[i][j] == "#":
                map_info[i][j] = 1
            elif map_info[i][j] == ".":
                map_info[i][j] = 0

    bfs(map_info)

if __name__ == "__main__":
    main()