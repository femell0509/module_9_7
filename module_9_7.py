def is_prime(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        is_prime = True
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                is_prime = False
        if is_prime == True:
            print('Простое')
        else: print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    _sum = 0
    for i in args:
        _sum += i
    return _sum

result = sum_three(2, 3, 6)
print(result)

def all_variants(text):
    s = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            s.add(text[i:j+1])
    l = list(s)
    l.sort()
    for i in l:
        yield i

for w in all_variants('abc'):
    print(w)