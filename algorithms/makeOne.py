#1로 만들기, 연산을 사용하는 횟수의 최솟값 출력
#최적 부분 구조, 중복되는 부분 문제를 만족 (피보나치)

x= int(input())

d=[0]*30001

for i in range(2,x+1):

    d[i]= d[i-1] + 1

    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)

    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)

    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)

print(d[x])



