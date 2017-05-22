# created : 2016.12.18
# author : Soon Gu Jung
# purpose : for testing the 'while' loop which i studied.

arr = [5,2,4,3,1,6];

print("before sorting ...")
print(arr)

i=0
while i<len(arr):
    j=i+1
    while j<len(arr):
        if arr[i]>arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        j=j+1
    i=i+1

print("after sorting ...")
print(arr)