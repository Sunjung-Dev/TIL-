N, x = map(int, input().split())
num_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    mid = (start + end) // 2

    if start > end :
        return None 

    if array[mid] == target:
        return mid
    
    elif target > array[mid]:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)


result = binary_search(num_list, x, 0, N-1)

if result == None:
    print('원소가 존재하지 않습니다 ')
else:
    print(result + 1)