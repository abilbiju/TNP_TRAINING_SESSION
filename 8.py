n=int(input())
stock=list(map(int, input().split()))
found=list(map(int, input().split()))
print(sum(stock)-sum(found))