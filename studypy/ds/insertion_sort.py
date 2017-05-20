#-*-coding:utf-8-*-
# created : 2016.12.22
# author : Soon Gu Jung
# purpose : for testing the 'while' loop which i studied.

# step
# 1) 정렬되지 않은 집합 A[0~i] 를 A[0~length-1] 까지로 검사범위를 넓혀간다
# 2) A[0~i]에 대해서 A[i+1]이 있어야 할 위치를 찾는다.
# 3) A[n->0]까지 A[i+1]값을 교환해 나간다.

# 배열의 모든 요소를 이미 정렬된 배열부분과 비교하여 알맞은 위치를 찾아 insert한다.
# 이미 정렬된 부분은 A(0~1), A(0~2), A(0~3).... , A(0~n)으로 차차 넓혀진다

arr = [1,5,2,4,3,6]

print("before sorting...")
print(arr)

i=0
j=0
while i<len(arr):
    j=i+1
    while j<len(arr) and j-1>=0:
        if(arr[j-1]>arr[j]):
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
        j-=1
    i+=1

print("after sorting...")
print(arr)

