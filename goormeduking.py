# https://level.goorm.io/exam/43266/%ED%99%A9%EC%A0%9C%EC%9D%98-%EB%AA%B0%EB%9D%BD/quiz/1

import sys

data = list(str(sys.stdin.readline()))
data.pop()
data = list(map(int, data))

M = max(data)+1

for i in range(M, 100):
    tot = 0
    for j in range(len(data)):
        tot += pow(i, j)*data[len(data)-1-j]
    if pow(tot, 0.5) - int(pow(tot, 0.5)) == 0:
        print(i)
        break
