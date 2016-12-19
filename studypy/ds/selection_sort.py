#-*-coding:utf-8-*-
# created : 2016.12.18
# author : Soon Gu Jung
# purpose : for testing the 'while' loop which i studied.

# step
# 1) 목록에서 최소값을 찾는다.
# 2) 찾은 최소값을 목록의 가장 맨 앞의 값과 바꾼다.
# 3) 정렬될 때 까지 이 과정을 반복한다.

arr = [5,2,4,3,1,6];
# min=0

print("before sorting ...")
print(arr)

i=0
while i<len(arr):
    j=i+1
    min = i
    while j<len(arr):
        if(arr[i] > arr[j]):
            min = j
            # min이 초기화되지 않고 이전에 찾아놓은 index인 경우도 있으므로
            # 바로 전 단계의 while문에서 min을 i로 바꿔줘야 한다.
            # ( 반복문의 each step마다 정렬되지 않은 나머지 배열의 첫요소를 가리켜야 하므로 )

        j=j+1
    temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp
    i=i+1

print("after sorting ...")
print(arr)