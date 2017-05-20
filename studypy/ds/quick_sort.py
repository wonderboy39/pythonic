#-*-coding:utf-8-*-
# created : 2016.12.22
# author : Soon Gu Jung
# purpose : for testing quicksort, partition function

arr = [5,3,2,4,8,1,6,7]
# left=0
# right=0
# pivot=0

print("----------------------------")
print("  before sorting  ... ")
print(arr)
print("----------------------------")

def swap(pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

def partition(start, end):
    # global pivot
    # global left
    # global right

    pivot = start
    left = start+1
    right = end
    done = False
    while left<right:
        while arr[left]<arr[pivot] and left<end:
            left+=1
        while arr[right]>arr[pivot] and right>start:
            right-=1
        if left<right:
            swap(left,right)
    swap(right, pivot)

    # do while을 사용할경우..
    # while not done:
    #     while left<end and arr[left]<arr[pivot]:
    #         left+=1
    #     while right>start and arr[right]>arr[pivot]:
    #         right-=1
    #     if left>right:
    #         done = True
    #     else:
    #         swap(left, pivot)
    # swap(right,pivot)

    return right


def quick_sort(start, end):
    if start<end:
        pos = partition(start, end)
        quick_sort(start, pos-1)
        quick_sort(pos+1, end)

quick_sort(0,len(arr)-1)
print("   after sorting ... ")
print(arr)
print("----------------------------")