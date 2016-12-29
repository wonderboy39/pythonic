#-*-coding:utf-8-*-
# created : 2016.12.28. pm 11:29
# author : Soon Gu Jung
# purpose : effective python, test codes...

# python에서 함수(function)의 기본적인 형태
# 함수(function) :
#   .코드의 재사용을 위한 존재
#   .일등시민(first class citizen)이다. (일급객체라는 말과 동일)
#    * 일등시민이 되기 위한 조건
#      - 객체를 변수에 할당가능해야 한다. (함수를 변수에 할당가능하다.)
#      - 객체를 인자로 전달가능 해야 한다. (다른 함수에 인자로 전달 가능하다.)
#      - 다른 객체가 리턴값으로 해당 객체를 받아낼 수 있어야 한다. (함수를 리턴값으로 받아낼 수 있다.)

# 함수의 매개변수 :
#   .모든 타입을 여러개 취할 수 있다.(일반 자료형,가변인자(*,**)

# 함수의 리턴값 :
#   .모든 타입을 여러개 반환할 수 있다.
#   .개수에 상관없이 모든 타입을 반환할 수 있다.
#   .만약 함수가 명시적으로 return을 호출하지 않을 경우 호출자(caller)는 None을 얻는다.

# 함수의 이름 :
#   .함수명은 영문자,숫자,언더스코어(_)만 가능하다.
#   .함수명의 첫글자는 영문자,_ 만 가능하다.

def do_nothing():
    pass

def agree():
    return True

if agree():
    print('Nice to meet you.')
else:
    print('Oh,no... False...')
print('')

# 함수가 명시적으로 return을 호출하지 않을 경우
print('print do_nothing()')
print(do_nothing())
print('')

# None에 대해서..
# None은 아무것도 없다는 것을 뜻하는 파이썬의 특별한 값이다.
# None이 부울로 평가될 경우 False로 보이지만 부울값의 False와는 다르다.
# 부울값과 None을 구분하기 위해서 is연산자를 사용한다. (중요 !!!!)
thing = None
if thing:
    print("It's some thing")
elif thing==False:
    print("It's False")
elif thing==None:
    print("It's None")
print('')


if thing is None:
    print("None")
elif thing:
    print('True')
else:
    print('False')

# 위치인자 (positional arguments)
# 함수의 매개변수는 정의해놓은 순서대로만 입력되어야 한다
# 정의해놓은 순서를 지키지 않으면 프로그래머의 부주의에 의한 의도치 않은 값이 입력된다.
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
menu('chardonnay', 'chicken', 'salad')

# 키워드 인자 (keyword argument)
# 위치인자의 혼동을 피하기 위해 정의해놓은 인자의 순서에 상관없이
# 매개변수에 상응하는 이름을 인자에 지정할 수 있다.
menu(entree='beef', dessert='chicken', wine='bordeaux')
# 위치인자와 키워드 인자를 섞어서 쓸수도 있다.
menu('frontenac', dessert='salad', entree='fish and chips')

# 기본 매개변수값 지정 (c++에서 볼수 있는 디폴트 매개변수...)
# 주의)
#   기본인자값은 함수가 실행될때 계산되지 않고 함수를 정의할 때 계산된다.
#   리스트 or 딕셔너리 등의 변경가능한 데이터타입을 기본인자로 사용할 때 예상치 못한 값이 들어갈 수 있다.
#   (파이썬을 처음 시작하거나 혹은 시간이 지난 프로그래머들이 자주하는 실수)
def menu(wine,entree, dessert='pudding'):
    return{'wine': wine, 'entree': entree, 'dessert':dessert}

print(menu('chardonnay', 'beef'))
print('')

# ex) 디폴트 매개변수로 인한 버그가 발생하는 예
def bug(input, fruits=[]):
    fruits.append(input)
    print(fruits)

bug('Avocado')
print('')

bug('Volcano')
print('')
# bug()를 실행할 때마다 비어있는 fruits 리스트에 input인자를 추가한 후
# fruits리스트를 출력하는 것이 의도였으나 예상과는 다르게
# 두번째로 호출하면 fruits리스트에는 이전 호출에서 생긴 한 항목이 들어있다.

# 이와 같은 현상을 해결하고자 할때 아래의 두가지 방식으로 해결이 가능하다
# 1) 전달되지 않을 매개인자에 대해 미리 디폴트 매개변수로 지정하지 않고 함수 내부에서 지역변수로 선언한다
# 2) 매개변수에 직접다른 값을 넣어서 디폴트값을 지정해 초기화하여 해결할 수도 있다.

# 1)
def works(fruit):
    fruits = []
    fruits.append(fruit)
    print(fruits)

# 2)
def works(fruit, fruits=None):
    if fruits is None:
        fruits = []
    fruits.append(fruit)
    print(fruits)

# 가변인자 ( *, ** )
# c,c++의 포인터와는 다른 개념
# * : 위치 인자 모으기, 함수는 위치인자들을 튜플로 묶어서 받는다
# ** : 키워드 인자 모으기, 함수는 키워드 인자를 덱셔너리로 묶을때 **를 사용한다.

# 함수의 가장 마지막에 *또는 **을 지정해서, 미리 정의된 필요한 매개변수들 외에
#   다른인자들의 전달도 허용할 수 있다.

# 1) * - 위치인자 모으기
# 입력값들을 튜플로 묶는다.
# 관용적으로 매개변수의 이름을 args를 사용한다.
# def print_args(*kwargs)
def print_fruits(*fruits):
    print('print positional aruments tuple, fruits : ' , fruits )
print_fruits(); #비어있는 튜플을 출력
print('')
print_fruits('Avocado','Banana','Cherry')
print('')

def print_fruits(city, country, *fruits):
    print('City : ', city)
    print('Country : ', country)
    print('Fruits : ', fruits)

# 2) ** - 키워드인자 모으기
# 키워드 인자를 딕셔너리로 묶기 위해 두개의 에스터리스크(**)를 사용할 수 있다.
# 관용적으로 매개변수의 이름을 kwargs를 사용한다.
def print_kwargs(**kwargs):
    print('Keyword arguments : ', kwargs)

# docstring
# '가독성은 중요하다(readibility counts).'는 파이썬의 철학이다.
# 함수의 몸체 시작 부분에 문자열을 포함시켜 함수정의에 documentation을 붙이는 것이 docstring이다.
# docstring은 길게 작성할수 있으며 서식(formatting)을 추가할 수도 있다.
# 작성한 docstring을 보고자 할때 help(함수명)을 통해 확인가능하다.
# docstring을 서식 없이 보고자 할때는 print(echo.__doc__) 로 출력가능하다.

def echo(anything):
    'echo returns its input arguments'
    return anything

def print_checked(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is ...
    :param thing: if check is true, thing would be printed.
    :param check: conditional variable.
    :return:
    '''
    if check:
        print(thing)

# docstring 출력
help(echo)
print('')

print(echo.__doc__)
# __doc__ 는 function 내부의 변수다.
print('')