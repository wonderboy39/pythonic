
# python의 함수
## python에서 함수(function)의 기본적인 형태
### 함수(function)
 * 코드의 재사용을 위한 존재
 * 일등 시민(first class citizen)이다. (일급객체라는 말과 동일)
 * 일등 시민이 되기 위한 조건
  1) 객체를 변수에 할당가능해야 한다. (함수를 변수에 할당가능해야 한다.)
  2) 객체를 인자로 전달가능해야 한다. (다른 함수에 함수를 인자로 전달가능하다.)
  3) 다른 객체가 리턴 값으로 해당 객체를 받아낼 수 있어야 한다. (함수를 리턴값으로 받아낼 수 있다.)

### 함수의 매개변수
모든 타입을 여러개 취할 수 있다. (일반 자료형, 가변인자( \* ,\*\* ) )

### 함수의 리턴값
모든 타입을 여러개 반환할 수 있다.  
개수에 상관 없이 모든 타입을 반환할 수 있다.  
만약 함수가 명시적으로 return을 호출하지 않을 경우 호출자(caller)는 None을 얻는다.  

### 함수의 이름
함수명은 영문자, 숫자, 언더스코어(_)만 가능하다.  
함수명의 첫글자는 영문자, _만 가능하다.  
ex)
```python
def do_nothing():
	pass
def agree():
	return True
if agree():
	print('Nixe to meet you')
else :
	print('Oh,no ... False')
print('')
```

### 함수에서 return을 명시하지 않을 경우
### 이 부분 책 한번 더 보고 정리할 것
```python
print('print do_nothing')
print(do_nothing())
print('')
```

### None에 대해서...
None은 아무것도 없다는 것을 뜻하는 python의 특별한 값이다.  
None이 Bool로 평가될 경우 False로 보이지만 Bool의 False와는 다르다.  
Bool과 None을 구분하기 위해 is연산자를 사용한다 (중요 !!!)  

```python
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
	print("True")
else:
	print("False")
```

### 위치인자 (positional arguments)
함수의 매개변수는 정의해놓은 순서대로만 입력되어야 한다.  
정의해놓은 순서를 지키지 않으면 프로그래머의 부주의에 의한 의도치 않은 값이 입력된다.  
```python
def menu(wine, entree, dessert):
	return {'wine':wine, 'entree':entree, 'dessert':dessert}
menu('chardonnay', 'chicken', 'salad')
```

### 키워드 인자 (keyword argument)
위치인자의 혼동을 피하기 위해 정의해놓은 인자의 순서에 상관없이 매개변수에 상응하는 이름을 인자에 지정할 수 있다.  
위치인자와 키워드 인자를 섞어서 쓸수도 있다.  
```python
# 매개변수에 상응하는 이름을 인자에 지정하는 경우
menu(entree='beef', dessert='chicken', wine='bordeaux')
# 위치인자와 키워드인자를 섞어서 쓸 경우
menu('frontenac', dessert='salad', entree='fish and chips')
```
### 디폴트 매개변수
#### 주의
 * 디폴트 매개변수의 값은 함수가 실행될 때 계산되지 않는다. 다만, 함수를 정의할 때 계산된다.
 * 리스트 / 딕셔너리 등 변경가능한 데이터 타입을 디폴트 매개변수로 사용할 경우 예상치 못한 값이 대입될 수 있다.(파이썬을 처음 시작하거나, 자주하는 실수)

ex) 디폴트 매개변수의 사용 예
```python
def menu (wine, entree, dessert='pudding'):
	print('default parameters')
	return ('wine': wine, 'entree': entree, 'dessert':dessert)
print(menu('chardonnay', 'beef'))
print('')
# 출력결과)
# default parameters
# {'dessert': 'pudding', 'entree': 'beef', 'wine': 'chardonnay'}
```

ex) 디폴트 매개변수로 인한 버그의 예
```python
def bug(input, fruits=[]):
    print('some bugs due to abused default parameters')
    fruits.append(input)
    print(fruits)

bug('Avocado')
print('')

bug('Volcano')
print('')
# 출력결과
# some bugs due to abused default parameters
# ['Avocado']
#
# some bugs due to abused default parameters
# ['Avocado', 'Volcano']
```
bug()를 실행할때마다 비어있는 fruits리스트에 input인자를 추가한 후 fruits리스트를 출력하는 것이 의도였으나 예상과는 다르게 두번째로 호출할 때 fruits리스트에는 이전 호출에서 생긴 한 항목이 들어있다.  
이와 같은 현상을 해결하고자 할 때 아래의 두가지 방식으로 해결이 가능하다.  
> * 전달되지 않을 매개인자에 대해 미리 디폴트 매개인자를 지정하지 않고 함수내부에서 지역변수로 선언한다.  
> * 매개변수에 직접 다른 값을 넣어서 디폴트값을 초기화하여 해결할 수도 있다.

ex) 해결방법 (1)
```python
def works(fruit):
	fruits=[]
    fruits.append(fruit)
    print(fruits)
```
ex) 해결방법 (2)
```python
def works(fruit, fruits=None):
	if fruits is None:
    	fruits = []
    fruits.append(fruit)
    print(fruits)
```
### 가변인자 (\*, \*\*)
c, c++에서 사용하는 포인터키워드와는 다른 개념이다.  
* \* : 위치인자 모으기, 함수 내부에서 위치인자들을 튜플로 묶어서 받는다.  
* \*\* : 키워드인자 모으기, 함수 내부에서 키워드 인자를 딕셔너리로 묶어서 받는다.  
* 함수의 가장 마지막에 \*, \**을 지정해서 미리 정의된 필요한 매개변수들 외에 다른 인자들의 전달을 튜플, 또는 딕셔너리로 전달받을 수 있다.

ex) \*을 이용한 위치인자 모으기
```python
'''
입력값들을 튜플로 묶는다.
가변인자의 이름은 관용적으로 args를 사용한다.
'''
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

print_fruits('Daegu', 'Korea', 'Apple, Grape, Cherry')
'''
출력결과 : 
('print positional aruments tuple, fruits : ', ())

('print positional aruments tuple, fruits : ', ('Avocado', 'Banana', 'Cherry'))

('City : ', 'Daegu')
('Country : ', 'Korea')
('Fruits : ', ('Apple, Grape, Cherry',))
Help on function echo in module __main__:
'''
```

ex) \*\*을 이용해 keyword arguments 모으기  
매개변수의 이름은 관용적으로 kwargs를 이용한다.  
나중에 자세히 다뤄볼 것  
```python
def print_kwargs(\*\*kwargs):
    print('Keyword arguments : ', kwargs)
```

### docstring
* '가독성은 중요하다(readability counts).'는 파이썬의 철학이다.  
* docstring은 함수의 몸체 시작부분에 문자열을 포함시켜 함수의 정의에 documentation을 붙이는 것이다.  
* docstring은 길게 작성할 수 있으며, 서식(formatting)을 추가할 수도 있다.  
* 작성한 docstring을 보려면 help(함수명)을 통해 확인가능하다.  
* docstring 을 서식 없이 보고자 할 때print(echo.\_\_doc\_\_)로 출력 가능하다.  





```python
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

# 함수 - 파이썬의 일등 시민
# : 함수는 변수에 할당할 수 있다.
# : 다른 함수에서 인자로 사용할 수 있다.
# : 다른 함수에서 함수를 반환할 수 있다.
# : ()는 파이썬에서 함수를 호출한다는 의미다.
# : ()가 없으면 함수를 다른 모든 객체와 마찬가지로 간주한다.
# : 함수에 ()없이 함수명만 인자로 전달하면 다른 모든 인자와 마찬가지로 이 함수를 데이터처럼 사용한다.

fruits = ['Avocado', 'Banana', 'Carrot']
def print_fruits():
    print(fruits)

def run_func(func):
    func()
    print('type(func) : ',type(func))

run_func(print_fruits)

# 함수와 함께 다른 인자들을 취하는 함수의 정의, 호출
def add_args(*args):
    return sum(args)
def call_func_with_args(func, arg1, arg2):
    print('sum of the func add_args : ', func(arg1, arg2) )
call_func_with_args(add_args, 3,9)
print('')
# 함수를 리스트,튜플,셋,딕셔너리의 요소로 사용할 수 있다.
# 함수는 불변이기 때문에 딕셔너리의 키로도 사용할 수 있다.

## 내부함수
# - 함수안에 또 다른 함수를 정의할 수 있다
# - 내부함수는 루프나 코드 중복을 피하기 위해 또 다른 함수내에
#   어떤 복잡한 작업을 한번 이상 수행할때 유용하게 사용된다

# ex) 그냥... 책에 쓰여있는 직관적인 예제..
def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)
outer(3,9)
print('')

# ex) 그냥... 책에 쓰여있는 직관적인 예제..
def knights(saying):
    def inner(quote):
        return "We are the knights who say : '%s'" %quote
    return inner(saying)


# 테스트 !!!) bubble_sort를 inner함수에서 수행하는 프로그램 작성
numbers = [6,5,4,3,2,1]
copied_numbers = list(numbers)
print copied_numbers
print('')

def outer(arr):
    def inner(arr2): # bubble sort in the inner function
        i=0
        while(i<len(arr2)):
            j=i+1
            while(j<len(arr2)):
                if(arr2[i]>arr2[j]):
                    temp=arr2[i]
                    arr2[i]=arr2[j]
                    arr2[j]=temp
                j+=1
            i+=1
    inner(arr)

outer(copied_numbers)
print('sorted copied_numbers : ', copied_numbers)

# 클로져
# 내부함수는 클로져(closure)처럼 동작할 수 있다.
# 클로저 :
#   특별한 함수다.
#   다른 함수에 의해 동적으로 생성된다.
#   outer함수로부터 생성된 변수값을 변경,저장할 수 있는 함수다.
#   outer함수로부터 생성된 변수값등을 변경,저장하는 내부 함수객체를 return해서 사용하기도 한다.

def knight2(saying):
    def inner2():
        return "We are the knights who say : '%s'" %saying
    return inner2

a = knight2('Darth Vader')
b = knight2('Yoda')

print(type(a))
print(type(b))

print(a)
print(b)
print(a())
print(b())

# 익명함수 : lambda()
# 파이썬의 람다(lambda function)는 단일문으로 표현되는 익명함수(anonymous function)이다.
# 람다식의 사용법)
#   lambda [매개인자1, 매개인자2, ...] : [계산식, 표현식, 처리문... --- 리턴값]
# ex)
#   lambda x,y : x+y
# 많은 경우 명확하게 함수를 정의해서 사용하는 것이 명확하다는 장점이 있다
# 람다를 사용하는 것은 많은 작은함수를 정의하고,
#    이들을 호출해서 얻은 모든 결과값을 저장해야 하는 경우에 유용하다.

# 1) 대문자로 만들기
def do_something(arg_list, func):
    for fruit in arg_list:
        print(func(fruit))

def capitalize(arg):
    return arg.capitalize() + '!'

print("1) Not using lambda")
do_something(fruits, capitalize)
print('')

print("2) Using lambda")
do_something(fruits, lambda word : word.capitalize() + '!')
print('')

# 2) get sum of numbers_to_sum , using lambda (annonymous function)
numbers_to_sum = [1,2,3,4,5,6,7,8,9,10]
def sum_numbers(arr_numbers, func):
    sum=0
    for number in arr_numbers:
        sum=func(number,sum)
    print('sum : ', sum)
sum_numbers(numbers_to_sum, lambda x,y: y+x)

# 제너레이터
```

