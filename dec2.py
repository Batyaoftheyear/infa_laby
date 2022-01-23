def dec_for_func(func):
    def wrapper(lst):
        a = func(lst)
        if a == 0:
            print('Нет')
        elif a > 10:
            print('Очень много')
        else:
            print(a)

    return wrapper
        
@dec_for_func
def chet(lst):
    k = 0
    for number in lst:
        if number % 2 == 0:
            k += 1
    return k


arr = list(map(int,input('Введите значения чисел через пробел ').split()))
dec_for_func(chet(arr))