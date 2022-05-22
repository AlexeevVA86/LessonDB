a = ['В', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
b = ['{:0>2}'.format(number) for number in a]

message = ''
for item in a:
    print(item, end=' ')