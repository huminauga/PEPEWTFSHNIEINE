# 5th task
def reverse(n):
    for i in range(n, -1, -1):
        yield i
N = int(input())
for x in reverse(N):
    print(x)