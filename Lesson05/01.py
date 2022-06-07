# 1. Написать генератор нечётных чисел от 1 до n (включительно)
# используя ключевое слово yield


def gen_nums_yield(num):
    for i in range(1, num + 1):
        if i % 2 == 1:
            yield i


print(*gen_nums_yield(15))
