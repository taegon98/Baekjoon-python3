import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while T:    #T리스트안에 데이터가 있을때까지 반복
    if T[-1] == 'A':    #if 'A' -> pop, 옵션1 : 리스트 뒤에 'A'추가
        T.pop()
    elif T[-1] == 'B':    #if 'B' -> pop and reverse, 옵션2 : 뒤집고 리스트 뒤에 'B'추가
        T.pop()
        T.reverse()
    if T==S:    #같은 경우면 1출력 -> 종료
        print(1)
        exit(0)
print(0)    #같게 될 수 없으면 0출력 -> 종료
