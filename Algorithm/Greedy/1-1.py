def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibo_for(n):
    result = []
    a, b = 1, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result[-1]


def solution(n):
    answer = 1
    fac = 1
    while fac <= n :
        answer += 1
        fac = fac * answer
    answer = answer-1
    print(answer)
    return answer

solution(120)