digit = 4535

def max_digit(some_digit):
    str_dig = str(some_digit)
    list_dig = list(str_dig)
    max_dig = max(list_dig)
    max_str = str(max_dig)
    max_int = int(max_str)
    print(max_int)


max_digit(digit)
