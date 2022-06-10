def gen_nums_no_yield(num):
    return (num for num in range(1, num + 1) if num % 2 == 1)


print(*gen_nums_no_yield(155))
