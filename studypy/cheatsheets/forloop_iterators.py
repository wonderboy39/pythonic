#-*-coding:utf-8-*-
# created : 2016.12.26
# author : Soon Gu Jung
# purpose : effective python, test codes...

# better way 10
#for loop로 list를 순회하는 방식 2가지

#just iterating integer set
print('Iterate integer set...')
for i in range(10):
    print(i)
print('')

#two ways how to iterate list
print('Just iterate list in two ways...')
print('1) Using for ~ in list')
fruits = ['Apple', 'Banana', 'Coconut', 'D...?']
for fruit in fruits:
    print(fruit)
print('')

print('2) Using for i in range(...)')
for i in range(len(fruits)):
    print(fruits[i])
print('')

# better way 11
# source list(names)에 표현식을 적용한 것을 derived list(letters)에 적용할 수 있다.
# (예제에서는 각 요소에 대한 문자열길이를 len(n)이라는 표현식으로 구한 결과를 letters에 저장했다)
# just using list comprehension
print('Just using list comprehension')
names = ['Alpha', 'Bravo', 'Charlie', 'Delta']
len_names = [len(n) for n in names]
print(len_names)
print('')

# ex) 표현식으로 구한 길이 리스트를 통해 길이가 names에서 가장 길이가 긴 요소를 찾기
print('Get max_length of string, using comprehension.')
longest_name = ''
max_size=0
for i in range(len(len_names)):
    temp_size=len_names[i]
    if temp_size > max_size :
        longest_name = names[i]
        max_size=temp_size
print(longest_name)
