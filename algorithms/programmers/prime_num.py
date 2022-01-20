#프로그래머스 알고리즘 문제
from itertools import combinations
import math

def prime_num(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True    

def solution(nums):
    answer = 0
    arr=list(combinations(nums,3))
    
    for i in arr:
        sum=i[0]+i[1]+i[2]
        if prime_num(sum):
            answer+=1
    return answer
