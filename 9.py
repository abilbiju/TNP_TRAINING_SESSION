n = int(input())
shows = [] 
for i in range(n):
    start, end = map(int, input().split())
    shows.append((end, start))

shows.sort()
#print(shows)
count = 0
current_end = -1
#print('[[[]]]')
for end, start in shows:
    if start >= current_end:
        count += 1
        current_end = end
        #print(end,start)

print(count)
