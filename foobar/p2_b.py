from fractions import Fraction

def solution(pegs):
    # Your code here
    l = len(pegs)
    if(not pegs or l == 1): 
        return [-1,-1]
    s = (pegs[l-1] - pegs[0]) if (l % 2 == 0) else (-pegs[l-1]-pegs[0]); 
    if(l > 2): 
        for i in range(1, l-1): s+= 2 * (-1)**(i+1) * pegs[i]
    v = Fraction(2*(float(s)/3 if (l%2==0) else float(s))).limit_denominator();
    c = v;
    for i in range(0, l-2):
        d = pegs[i+1] - pegs[i]
        n = d - c
        if(c < 1 or n < 1): 
            return [-1,-1]
        else:
            c = n
    return v.numerator, v.denominator;

print(solution([4, 30, 50]))