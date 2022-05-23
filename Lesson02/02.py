# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
# 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и
# дополнить нулём до двух целочисленных разрядов:

weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
weather2 = []
for i in range(len(weather)):
    circumcision = weather.pop(0)
    if  circumcision.isdigit():
        weather2.append(F'"{int(circumcision):02d}"')
    elif circumcision[0] == "-":
        weather2.append(F'"{int(circumcision):03d}"')
    elif circumcision[0] == "+":
        weather2.append(F'"+{int(circumcision):02d}"')
    else:
        weather2.append(circumcision)
print(' '.join(weather2))