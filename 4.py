#4. determine for a given p number of queens no tow queens are in attacping positions
n = int(input())
queens = [0] * n

def isSafe(row, col):
    for i in range(row):
        if queens[i] == col or abs(queens[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == n:
        return True  
    for col in range(n):
        if isSafe(row, col):
            queens[row] = col
            if solve(row + 1):
                return True
    return False

print(solve(0))
print(queens)


n=int(input())
chess=[[0]*n]*n
def isAttacking(i,j):
        for p in range(n):
            if chess[p][j] == 1 or chess[i][p] == 1:
                return True
        for p in range(n):
            if (p+1==i+j or p-1==i-j):
                if chess[p][1]==1:
                    return True
        return False
def nqueens(n):
    if n==0:
        return True
    for i in range(n):
        for j in range(n):
            if (not isAttacking(i,j)) and chess[i][j] != 1:
                chess[i][j] = 1
                if nqueens(n-1):
                    return True
                chess[i][j] = 0
        return False
print(nqueens(n))