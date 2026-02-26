# 1st task
def generator_square(a):
    for i in range(1, a+1):
        yield i * i
n = int(input())
for x in generator_square(n):
    print(x)