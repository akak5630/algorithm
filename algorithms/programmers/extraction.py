#프로그래머스 두 수 뽑아서 더하기 알고리즘
from itertools import combinations
def solution(numbers):
    answer = []
    a = list(combinations(numbers, 2))
    
    for i in a:
        answer.append(i[0]+i[1])
        answer = list(set(answer))
        answer.sort()
    
    return answer
