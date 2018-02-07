#problem :
#https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
#solution
import collections as col
def solution(A):
    # write your code in Python 3.6
    freq=col.Counter(A)
    unpaird=0
    for key in freq:
        if freq[key]%2!=0:
            unpaird=key
    return unpaird
    pass
