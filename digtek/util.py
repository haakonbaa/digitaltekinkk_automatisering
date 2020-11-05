"""En sambling av ofte brukte funksjoner som brukes i flere moduler"""

__all__ = ["binary_to_number","number_to_binary"]

# INPUT: CSV 1/0, MSB først
# OUTPUT: int
def binary_to_number(*args):
    s = 0
    r = 0
    for i in args[::-1]:
        s += i*2**r
        r += 1
    return s

# INPUT: int, int
# OUTPUT tuple(): 0/1
def number_to_binary(number,length):
    ans = []
    for i in range(length):
        remainder = number % 2
        number //= 2
        ans.insert(0,remainder)
    return tuple(ans)

LAMBDA = lambda: 0
def is_lambda(var):
    return isinstance(v, type(LAMBDA)) and v.__name__ == LAMBDA.__name__
