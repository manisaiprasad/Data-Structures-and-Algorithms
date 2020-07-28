def solution(start, length):
    # Your code here
    result=0
    for i in range(0, length):
        a = start+(length*i)
        b = start+(length*i)+(length-i)-1
        if(a%2==0):
            xor_rotation = [b, 1, b+1, 0]
        else:
            xor_rotation= [a, a^b, a-1, (a-1)^b]
        result ^= xor_rotation[(b-a)%4]
    # return result
    return result
print(solution(17, 4)) #should return 14