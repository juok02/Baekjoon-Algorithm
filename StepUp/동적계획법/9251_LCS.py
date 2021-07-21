'''
######문제######
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.


######입력######
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.


######출력######
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.


((((((((ex))))))))
입력| ACAYKP
   | CAPCAK

출력| 4

'''


#code
x = list(input())
y = list(input())
x_len = len(x)
y_len = len(y)
d = [[0] * (y_len + 1) for _ in range(x_len + 1)]

for i in range(1, x_len + 1):
  for j in range(1, y_len + 1):
    if x[i-1] == y[j-1]:
      d[i][j] = d[i-1][j-1] + 1
    else:
      d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[-1][-1])






    