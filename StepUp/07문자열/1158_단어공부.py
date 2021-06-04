'''
#문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

#입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

#출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

ex)
입력| Mississipi    zZa     baaa

출력|     ?          Z        A
'''

#code
word = input().upper()
set_word = list(set(word)) #중복없는 리스트를 만든다.

count_list=[]
for i in set_word:
  count_list.append(word.count(i)) #순서대로 count를 센다

if count_list.count(max(count_list)) > 1: #많이 사용된 알파벳이 여러개일 경우
    print("?")
else:
    index = count_list.index(max(count_list)) #index(): 리스트에 값이 있으면 해당 인덱스를 반환한다.
    print(set_word[index])