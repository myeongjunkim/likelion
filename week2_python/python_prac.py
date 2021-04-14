# # 파이썬 코드 실습


# # 자료형(리스트, 튜플, 딕셔너리)

# # 리스트(List): 순서o, 중복o, 수정o, 삭제o
# # 선언
# a = []
# b = list()
# c = [1,2,3,4]
# d = [1, 10, 'apple']
# e = [1,1,1,1,[1,2]]

# # 인덱싱: 인덱스를 이용해 리스트 안에서 특정한 값을 가져옴
# print(c[0])



# # 슬라이싱: 인덱스를 이용해 일부분을 잘라서 가져옴
# print(d[2:])

# # 추가, 수정, 삭제
# # 추가: append, extend
# a.append(3)
# a.append([4,5,6])
# print(a)

# a.extend([4,5,6])
# print(a)
# # 수정


# # 삭제: remove, pop, del
# # a.remove(value)
# # a.pop(index) #뭐 삭제 했는지 반환
# del a[1] #반환 nono

# # +a
# # 리스트 길이: len
# print(len(a))
# # 정렬: sort
# a.sort()



# print('----------------------------------------')

# # 튜플(Tuple): 순서o, 중복o, 수정x, 삭제x 
# # 변경되는 것을 방지하기 위해 중요데이터를 관리할 때 사용
# # 선언

# a=(1,)
# b=(1,2,3,4)


# print('----------------------------------------')

# # 딕셔너리(Dictionary): 순서x, 중복x, 수정o, 삭제o
# # Key(변함x), Value(변함o, 변함x)
# # 선언
# a = {'name':'Kim','Phone':'010-9999-9999'}
# b = {0:"hello", 1:"coding"}
# c = {"arr" : [1,2,3,4,5]}

# # 추가
# a['School'] = 'Chung-ang'
# print(a)

# # keys, values, items, get(key&value 한쌍)

# print('----------------------------------------')

# # 조건문(if-else)
# arr1 = [0,1,2,3,4,5,6]

# if 0 in arr1:
#     print(0)
#     if 10 not in arr1:
#         print('no 10')
# elif 3 in arr1:
#     print(3)
# else
#     print("Nothing")

# print('----------------------------------------')

# # 반복문
# # 기본 반복문: for, while

# for v2 in range(10):
#     print("v2: ", v2)



# # 순서 있는 자료형 반복
# # 문자열, 리스트, 튜플, 집합, 사전
# # iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# my_info = {
#     "name" : "oh",
#     "age" : 23,
#     "city" : "Seoul"
# }

# for key in my_info.keys():
#     print("키: ", key)


# # 기본 값은 키


# # keys


# # values
# # my_info.values()

# # items 둘다


# # enumerate: 반복 횟수
# p = [1,2,3,4,5]
# for i in enumerate(p):
#     print(i)
# # break



# print('----------------------------------------')

# # 예외처리(try-except)

# try:
#     4/0
# except IndexError:
#     print("인덱스 에러")
# except ZeroDivisionError as e:
#     print(e)

# print('----------------------------------------')

# 함수
# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

def func(word):
    print("hello", word)

func("world")

# 코드상에서 명시적으로 자료형이나 반환값 힌트를 주기
def func(x : int) -> list:
    y1 = x + 100
    y2 = x + 200
    return [y1,y2]

print(func(10))


print('----------------------------------------')

# 모듈
# 함수나 변수 또는 클래스를 모아 놓은 파일

# 선언
# import 모듈이름
# from 모듈이름 import 모듈함수


'''
rlaaudwns
'''

import datetime

print(datetime.datetime.today())

from datetime import datetime
print(datetime.today())

import random
print(random.randint(1,200))

from random import shuffle
arr = [1,2,3,4,5]

shuffle(arr)

print(arr)