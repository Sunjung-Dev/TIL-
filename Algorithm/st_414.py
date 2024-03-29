def main():
    N, K = map(int, input().split())
    rail = list(map(str, input()))

    answer = 0
    visited = [0] * (N+1)

    for i in range(N):

        for j in range(K, 0, -1):
            if i+j >= N:
                continue

            if visited[i] == 0 and visited[i+j] == 0:

                if rail[i] == 'P' and rail[i+j] == 'H':
                    visited[i] = 1
                    visited[i+j] = 1
                    answer += 1

                if rail[i] == 'H' and rail[i+j] == 'P':
                    visited[i] = 1
                    visited[i+j] = 1
                    answer += 1
    print(answer)
    return answer

if __name__ == "__main__":
    main()