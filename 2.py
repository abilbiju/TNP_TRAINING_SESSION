#2 test for a palindrome for any of its permutation
s = input().strip().lower()
cf = {}
for ch in s:
    if ch in cf:
        cf[ch] += 1
    else:
        cf[ch] = 1

oc = 0
for freq in cf.values():
    if freq % 2 != 0:
        oc += 1

if oc > 1:
    print("NO")
else:
    print("YES")

#provided solution
from collections import Counter
s = input().strip().lower()
count = Counter(s)
cd={}
co=0
for i in cd.values():
    if i%2==0:
        co+=1
if co>1:
    print("NO")
else:
    print("YES")