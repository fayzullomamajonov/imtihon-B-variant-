from time import time

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

@timer_func
def tub_sonlarni_top(son):
    tub_sonlar = []
    for i in range(2, son + 1):
        tub = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                tub = False
                break
        if tub:
            tub_sonlar.append(i)
    return tub_sonlar

@timer_func
def call_tub_sonlarni_top():
    son = int(input("Ixtiyoriy son kiriting: "))
    return tub_sonlarni_top(son)

call_tub_sonlarni_top()

#'call_tub_sonlarni_top' = 3.6860s