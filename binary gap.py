def solution(N):
    # write your code in Python 3.6
    x=str(bin(N)[2:])
    f,b=0,0
    #my approach needs to remove trailing zeros from front and back of the pattern
    for i in range(0,len(x)-1):
        if(x[i]=='0'):
            f+=1
        elif(x[i]=='1'):
            break
    for i in range(0,len(x)-1):
        if(x[len(x)-1-i]=='0'):
            b+=1
        elif(x[len(x)-i-1]=='1'):
            break
    if(f!=0 or b!=0):
        y = x[f:len(x) - 1 - b]
    else:y=x
    y=y.split("1")
    y.sort()
    count=0
    for c in y[-1]:
        count += 1
    return count
    pass
