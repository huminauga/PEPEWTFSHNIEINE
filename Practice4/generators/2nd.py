# 2nd task
def even(a):
    for i in range(0, a+1):
        if i % 2 == 0:
            yield i

n = int(input())

first = True
for x in even(n):
    if not first:
        print(",", end=" ")
    print(x, end="")
    first = False