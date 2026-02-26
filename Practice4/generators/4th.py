# 4th task
def squares(a, b):
    for i in range(a, b+1):
        yield i * i
x, y = int(input()), int(input())
for x in squares(x, y):
    print(x)