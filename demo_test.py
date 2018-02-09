import time
import random


def solution(A):
    # write your code in Python 3.6
    if 1 not in A:
        return 1

    A.sort()
    if A[-1] < 0 :
        return 1
    
    if len(A)==1:
        return A[0]+1

    for x in range(A.index(1), len(A)-1):
        if A[x+1] != A[x]:    
            if A[x+1] - A[x] != 1:
                return A[x]+1

    return A[-1]+1


#gg=range(-1000, 40000)
gg=range(1,40000)
#gg=[4, 1, 5, 6, 2]  # 3
#gg=[1, 3, 6, 4, 1, 2]  # 
#gg=[1, 2, 3] 
#gg=[-1, -3] 
#gg=[4, 5, 6, 2]
#gg=[2,6,1,-999, 54,123114123,0]

random.shuffle(gg)
x=time.time()
print solution(gg)
print time.time()-x


'''
Detected time complexity:
O(N) or O(N * log(N))
collapse allExample tests
? example1 
first example test ?OK
1. 0.036 s OK
? example2 
second example test ?OK
1. 0.036 s OK
? example3 
third example test ?OK
1. 0.036 s OK
collapse allCorrectness tests
? extreme_single 
a single element ?OK
1. 0.036 s OK
2. 0.036 s OK
3. 0.036 s OK
4. 0.036 s OK
? simple 
simple test ?OK
1. 0.036 s OK
2. 0.036 s OK
3. 0.036 s OK
? extreme_min_max_value 
minimal and maximal values ?OK
1. 0.036 s OK
2. 0.036 s OK
? positive_only 
shuffled sequence of 0...100 and then 102...200 ?OK
1. 0.036 s OK
2. 0.036 s OK
? negative_only 
shuffled sequence -100 ... -1 ?OK
1. 0.036 s OK
collapse allPerformance tests
? medium 
chaotic sequences length=10005 (with minus) ?OK
1. 0.044 s OK
2. 0.048 s OK
3. 0.044 s OK
? large_1 
chaotic + sequence 1, 2, ..., 40000 (without minus) ?OK
1. 0.140 s OK
? large_2 
shuffled sequence 1, 2, ..., 100000 (without minus) ?OK
1. 0.180 s OK
2. 0.172 s OK
? large_3 
chaotic + many -1, 1, 2, 3 (with minus) ?OK
1. 0.148 s OK

'''
