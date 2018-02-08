#problem:https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
#Solution
#you code time complexity must be O(N)
def solution(A):
    # write your code in Python 3.6
    return(sum(range(1,len(A)+2))-sum(A))
    pass
