def fib(n):
    a,b = 1,1
    for _ in range(0,n):
        a, b = b, a + b
    return a

def solution(total_lambs):
    # Your code here
    generous = 1
    while True:
        total = 2**(generous) - 1
        if total <= total_lambs:
            generous += 1
        else:
            generous -= 1
            break
        
    stingy = 1
    while True:
        total = (fib(stingy + 2) - 1)
        if total <= total_lambs:
            stingy += 1
        else:
            stingy -= 1
            break

    comp = [generous, stingy]
    diff = max(comp) - min(comp)
    return diff+1

#tests
print(solution(143))
print(solution(10))
print("Pass" if (solution(143)==3) else "fail")
print("Pass" if (solution(10)==1) else "fail")
