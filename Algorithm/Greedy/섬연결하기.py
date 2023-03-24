# Minimum Spanning Tree 문제.

# Kruskal Algorithm 사용.

# union and Find 함수 짜기

root=[]

#Initialization 
def make_set(n, root):
    root.extend([element for element in range(n)])
    
    
def find(x):
    if root[x] !=x:
        return find(root[x])
    
    return x

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        root[y] =x
    else:
        root[x] =y
#Initialization        
    
# root= [element for element in range(n)]

def solution(n, costs):
    sorted_cost=sorted(costs, key = lambda x: x[2])
    tree_edges=0
    answer=0
    make_set(n,root)
    # for element in range(n):
    #     root.append(element)
    while tree_edges < n-1:  # Spanning Tree의 정의
        for info in sorted_cost: #Cycle인지 아닌지 여부
            if find(info[0]) == find(info[1]):
                continue
            else:
                union(info[0],info[1])
                answer+= info[2]
                tree_edges+=1                
    return answer
