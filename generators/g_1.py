def gen_for_fib (k):
    m, n = 0, 1
    while True:
        yield m
        k -= 1
        m, n = n, m+n
        if k==0:
            break

for i in gen_for_fib(5):
    print(i, end = ' ')