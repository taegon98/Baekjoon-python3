import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while True:
    if T[-1] == 'A':
        T.pop(len(T) - 1)
    elif T[-1] == 'B':
        T.pop(len(T) - 1)
        if T:
            T.reverse()
    if not T:
        print(0)
        break
    if T==S:
        print(1)
        break