# 3. *(вместо задачи 2) Решить задачу 2 не создавая новый список

weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(weather)):
    circumcision = weather.pop(0)
    if  circumcision.isdigit():
        weather.append(F'"{int(circumcision):02d}"')
    elif circumcision[0] == "-":
        weather.append(F'"{int(circumcision):03d}"')
    elif circumcision[0] == "+" and circumcision[1].isdigit():
        weather.append(F'"+{int(circumcision):02d}"')
    else:
        weather.append(circumcision)
print(' '.join(weather))