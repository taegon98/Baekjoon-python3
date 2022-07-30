import sys
from itertools import permutations
n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
temp = list(map(int,sys.stdin.readline().split()))
oper = ['+','-','*','/']    #실제 연산자가 들어있는 리스트로 바꾸기 위해 사용
result = []    #계산 결과 저장 리스트
op = []    #실제 연산자가 갯수만큼 들어있는 리스트

for i in range(len(temp)):  
    for j in range(temp[i]):    #각 연산자의 갯수만큼 for문을 돌면서
        op.append(oper[i])    #실제 해당하는 연산자를 해당 갯수만큼 op리스트에 추가
#실제 연산자가 갯수만큼 들어있는 리스트의 n-1순열
for i in list(permutations(op,n-1)):
    index = 1    #첫번째수는 tot에 저장하므로 1부터 시작
    tot = num_list[0]    #tot에 첫번째 값을 저장하고 계속해서 누적
    for j in i:
        if j == '+':
            tot = tot + num_list[index]
        if j == '-':
            tot = tot - num_list[index]
        if j == '*':
            tot = tot * num_list[index]
        if j == '/':
            tot = int(tot / num_list[index])    #몫만 계산
        index+=1
    result.append(tot)    #모든 계산의 경우 저장
print(max(result))
print(min(result))