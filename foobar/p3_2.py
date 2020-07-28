def solution(l):
    # Your code here
    result = 0
    pair = [0]*len(l)
    for i in range(1, len(l)-1):
        for j in range(i):
            if(l[i]%l[j]==0):
                pair[i]+=1
    for i in range(2, len(l)):
        for j in range(1, i):
            if(l[i]%l[j]==0):
                result += pair[j]
    return result 