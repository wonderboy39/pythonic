
arr = [1,4,5,2,3,6]

print("before sorting...")
print(arr)
i=0
#for i, val in enumerate(sequence, start=0)
print("\nsorting...")
while i<len(arr):
	j=i+1
	while j<len(arr) :
		if arr[i]>arr[j]:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
		j= j+1
	print(arr)
	i+=1
# print(arr)
print("\nafter sorting...")
print(arr)