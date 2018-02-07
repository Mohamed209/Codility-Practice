#problem : https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
#Solution :
def solution(a):
    p = []
    for i in range(0, len(a) - 1):
        p.append(abs(sum(a[0:i + 1]) - sum(a[i + 1:])))
    p.sort()
    return p[0]
