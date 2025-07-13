l=list(map(int,input().split()))
n,items=l[0],l[1]
l=list(map(int,input().split()))
k=items

# for i in range(n - k + 1):
#     print(max(l[i:i + k]), end=' ')
# print()

dequeue=[]

def pop_front():
    if dequeue:
        dequeue.pop(0)
def pop_back():
    if dequeue:
        dequeue.pop()  
def push_back(x):
    dequeue.append(x)
def push_front(x):
    dequeue.insert(0,x)
push_front(max(l[0:k]))

for i in range(k):
    while dequeue and l[i] >= l[dequeue[-1]]:
        pop_back()
    push_back(i)

for i in range(k, n):
    print(l[dequeue[0]], end=' ')

    if dequeue and dequeue[0] <= i - k:
        pop_front()

    while dequeue and l[i] >= l[dequeue[-1]]:
        pop_back()

    push_back(i)

print(l[dequeue[0]])

 