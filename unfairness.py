# You will be given a list of integers, arr, and a single integer k. You must sort the numbers in ascending order and create an array of length k from elements of arr to minimize its unfairness. Call that array arr'. Unfairness of an array is calculated as = max(arr') – min(arr')

l=list(map(int,input().split(',')))
k=int(input())

# Sort the list first
l.sort()
min_unfairness = float('inf')
best_left = 0

# Try all possible subarrays of length k
for i in range(len(l) - k + 1):
    current_unfairness = l[i + k - 1] - l[i]
    if current_unfairness < min_unfairness:
        min_unfairness = current_unfairness
        best_left = i

# Select the subarray with minimum unfairness
l = l[best_left:best_left + k]
l=sorted(l)
uf=max(l)-min(l)
left=0
right=k
ans=l[left:right]

for i in ans:
    print(i,end=' ')
        
