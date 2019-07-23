# 斐波那契数模块

# 打印斐波那契数直到 n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, b + a
    print()

# 返回到 n 的斐波那契数
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
