# sliding window maximum
# Given an array of integers and a number k, find the maximum for each and every contiguous subarray of size k.

l=list(map(int,input().split()))
n,items=l[0],l[1]
snacks=list(map(int,input().split()))
# k=0
# section_sum=0
# while k<n:
#     section_sum=max(section_sum,sum(snacks[k:k+items]))
#     k+=items
# print(section_sum)


i=0
k=items
max_sum=current_sum=sum(snacks[i:k])
while k<n:
    current_sum=current_sum-snacks[i]+snacks[k]
    max_sum=max(max_sum,current_sum)
    i+=1
    k+=1
print(max_sum)