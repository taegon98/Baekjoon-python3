import sys
N = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
result = [False for _ in range(2000001)]    #최대 수 100,000 * 최대 수열 크기 20개
def sum(index, tot):
    if index >= N: return    #범위를 벗어나면 종료
    tot += l[index]

    result[tot] = True    #합에 해당하는 index 방문처리
    #모든 경우의 수 고려(트리로 도식화)
    sum(index+1, tot)    #포함하는 경우
    sum(index+1, tot-l[index])    #포함하지 않는 경우

sum(0,0)
for i in range(1, len(result)):    #자연수 1부터 최대수까지 탐색
    if result[i] == False:    #방문한적 없는 숫자 중에서 가장 작은 자연수 출력 후 break
        print(i)
        break