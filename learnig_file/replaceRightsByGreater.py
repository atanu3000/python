arr = [17, 18, 5, 4, 6, 1]

for i in range(len(arr)-1):
    for j in range(len(arr)):
        if (j < i and arr[j] < arr[i]):
            arr[j] = arr[i]
    arr[i] = arr[i+1]
arr[-1] = -1

print(arr)