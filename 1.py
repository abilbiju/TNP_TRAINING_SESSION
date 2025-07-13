# #1. Print k number of prime nmbers
# n=int(input())
# for i in range(2,n+1):
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')
# print('\n')


# #PROVIDED SOLUTION 1

# def is_prime(num):
#     for i in range(2, int(num//2) + 1):
#         if num % i == 0:
#             return False
#     return True
# n = int(input("Enter a number: ").rstrip())
# for i in range(2, n + 1):
#     if is_prime(i):
#         print(i, end=' ')
# print('\n')

# #PROVIDED SOLUTION 2
# def markFalse(a,n):
#     for k in range(a,n+1,a):
#         isPrime[k]=False

# n=int(input())
# primes=[]
# isPrime=[True]*(n+1)
# isPrime[0]=isPrime[1]=False
# primes.append(2)

# markFalse(2,n)
# for i in range(3, n+1 , 2):
#     if isPrime[i]==True:
#         primes.append(i)
#         markFalse(i,n)
# print(primes)

#PROVIDED SOLUTION 3
def markFalse(a,n):
    p=2*a+3
    start = (p*p - 3) // 2
    for k in range(start,size,p):
        isPrime[k]=False

n=int(input())
primes=[2]
size=int(0.5*(n-3)+1)
isPrime=[True]*size

for i in range(size):
    if isPrime[i]:
        primes.append(2*i+3)
        markFalse(i,n)
print(primes)  