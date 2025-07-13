# #3. find numbe of zeroes in the number set 1 to n
n=int(input())
c=0
for i in range(1, n + 1):
    c+= str(i).count('0')
print(c)    

# #ANAND SOLTN
a=int(input())
c=0
l=len(str(a))-1
m=l
while m>1:
    c+=9*(m-1)*10**(m-2)
    m-=1
for i in range(10**l,a+1):
    c+=str(i).count('0')
print(c)

#PROVIDEED SOLUTION
def countZeroes(n):
    result = 0
    digit = 1
    while True:
        posVal, rem = divmod(n, digit)
        prefix, posval = divmod(posVal, 10)

        if posVal == 0:
            return result

        if posval == 0:
            result += (prefix - 1) * digit + rem + 1
        else:
            result += prefix * digit

        digit *= 10

    return result

n = int(input())
print(countZeroes(n))
