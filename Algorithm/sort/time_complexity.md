# 배열의 시간복잡도 

```py
def solution(players, callings):
    answer = []
    
    for i in range(len(callings)):
        idx = players.index(callings[i])
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    print(players)
    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
```

### index()
``` py
players.index(callings[i]) 
```
- 여기서 요소의 index를 확인하는 index메소드는 시간복잡도 O(n)인데 왜 시간초과가 발생할까? 
