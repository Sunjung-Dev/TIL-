import itertools

#permuatation, 순열 
arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

#combination, 조합 
nCr = itertools.combinations(arr, 2)
print(list(nCr))


#permutation, combination을 사용하면서 유용한 함수 
#zip()
# 동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어서 Iterator로 반환 
z = zip([1, 2, 3], ('A', 'B', 'C'))
print(next(z))
