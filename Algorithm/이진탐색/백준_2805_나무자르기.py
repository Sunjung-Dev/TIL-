N, M = map(int, input().split())
tree_weight = list(map(int, input().split()))

def binary_search(array, target, start, end):
    # total = 0
    result = list()
    
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for x in array:
            if x > mid:
                total += x - mid
        if total < M:
            end = mid - 1
        
        # total >= M 인 경우 
        else:
            result.append(mid)
            start  = mid + 1

    return max(result)


result = binary_search(tree_weight, M, 0, max(tree_weight))
print(result)