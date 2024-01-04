import sys

def iter_lst(func):
    sort_lst = []
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for element in result:
            if type(element) == int:
                sort_lst.append(element)
        x = sorted(sort_lst[:])
        return x
            

        # return result

    return wrapper

@iter_lst
def iter_fun():
    lst = [1, 2, 5, 3, 'ali', 'vali', 16]
    iter_lst = iter(lst)
    return iter_lst

print(iter_fun())
