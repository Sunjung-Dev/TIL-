A, B = map(int, input().split())

def driven_distance(A, B):
    if A > B:
        return "A"
    if A < B:
        return "B"
    if A == B:
        return "same"

print(driven_distance(A, B))