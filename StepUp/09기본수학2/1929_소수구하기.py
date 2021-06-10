'''
#문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

#입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

#출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

ex)
입력| 3 16

출력| 3
   | 5
   | 7
   | 11
   | 13
'''


#code
M, N = map(int, input().split())

for num in range(M, N+1):
  error = 0
  if num != 1:
    for i in range(2,int(num**0.5)+1): #제곱근까지만 계산
      if num%i == 0:
        error += 1
        break
    if error == 0:
      print(num)





    