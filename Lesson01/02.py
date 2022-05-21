# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):..

list_number: list[int] = []
numbers = range(1, 1001)
for num in numbers:
    if num % 2 == 1:
        num = num ** 3
        list_number.append(num)
print(list_number)
result_sum = 0
for num in list_number:
    temp_num = num
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    if sum % 7 == 0:
        result_sum += temp_num
print(result_sum)
result_sum2 = 0
for num2 in list_number:
    num2 = num2 + 17
    temp_num2 = num2
    sum2 = 0
    while (num2 != 0):
        sum2 = sum2 + num2 % 10
        num2 = num2 // 10
    if sum2 % 7 == 0:
        result_sum2 += temp_num2
print(result_sum2)
