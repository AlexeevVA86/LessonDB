# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
# 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и
# дополнить нулём до двух целочисленных разрядов:


word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# for word in word_list:
#     found_num = []
#     for symb in word:
#         if symb in digits:
#             found_num.append(symb)
#         else:
#             if len(found_num) > 0:
#                 print("Found number {:0>2}".format(''.join(found_num)))
#     if len(found_num) > 0:
#         print("\"" + "{:0>2}".format(''.join(found_num)) + "\"")

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 1
while i < len(my_list):
    my_list.insert(i, '"')
    i += 2
