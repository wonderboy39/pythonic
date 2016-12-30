#-*-coding:utf-8-*-
# created : 2016.12.30. at the office... 몰래 몰래 공부즁...ㅋㅋ
# author : Soon Gu Jung
# purpose : introducing python, test codes...


# 제너레이터
#   파이썬에서 시퀀스를 생성하는 객체
#   제너레이터를 사용하면 전체 시퀀스를 한번에 메모리에 생성하고 정렬할 필요없이
#   잠재적으로 아주 큰 시퀀스(1,2,3,4,....n 과 같은 일련의 숫자조합)를 순회할 수 있다.
#   이터레이터에 데이터의 소스로 자주 사용되는 편이다.
#   제너레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음값을 반환한다.

#   파이썬2의 range():
#       range() - 제한적인 리스트를 반환
#       xrange() - 파이썬3의 일반적인 range()처럼 쓰인다.
#
#   파이썬3의 range():
#       파이썬2의 xrange()처럼 쓰인다.

sum = sum(range(1,11))
print(sum)

# 제너레이터 함수
# 잠재적으로 큰 시퀀스를 생성하고, 제너레이터 컴프리헨션에 대한 코드가 긴 경우 제너레이터 함수를 사용한다.
# range()와 같은 결과를 얻기 위해 일반 함수이지만 return문으로 값을 반환하지 않고 yield문으로 값을 반환한다.
# (return은 함수 자체를 반환하면서 종료하기 때문에 )
# ex)
def custom_range(start=0, end=10, seq=1):
    number = start
    while number<end:
        yield number
        number+=seq

for i in custom_range(0,3,1):
    print(i)

print(custom_range)
crange = custom_range(0,8,1)
print(crange)

#ex) 제너레이터를 활용해서 0~10까지의 홀수를 출력해보자.
def odd_range(start=1, end=10, seq=2):
    n=start
    while n<end:
        yield n
        n+=seq

for i in odd_range():
    print(i)

# 데커레이터
