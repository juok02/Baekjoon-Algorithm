'''
#문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

#입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

#출력
주어진 수들 중 소수의 개수를 출력한다.

ex)
입력| 4
   | 1 3 5 7

출력| 3
'''


#code
n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num): 
            if num % i == 0:
                error += 1
                break;
        if error == 0:
            sosu += 1  
print(sosu)





    