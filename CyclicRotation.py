#problem : https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
#Solution :
def solution(A, K):
    # write your code in Python 3.6
    if A ==[]:
        return 0
    else:
        for x in range(K):
            temp = A[-1]
            for i in range(0, len(A)):
                A[len(A) - i - 1] = A[len(A) - i - 2]
            A[0] = temp
    return A
    pass
