# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

duration: int = int(input())
if duration // 60 == 0:
    print (duration , "сек")
elif 0 < (duration // 60) < 60:
    print(duration // 60, " Мин ", duration % 60, " сек")
elif 0 >= duration // 3600 or duration // 3600 >= 24:
    print(duration // 86400, "дн", (duration % 86400) // 3600, "час", duration % 86400 % 3600 // 60, " Мин", duration % 86400 % 3600 % 60,  " сек")
else:
    print(duration // 3600, 'час', (duration % 3600) // 60, "мин", duration % 3600 % 60, " сек")
