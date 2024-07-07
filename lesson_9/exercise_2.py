# lesson_9 exercise 2 https://lms.synergy.ru/practicums/attempt/5025993/1?groupPeriodId=1166613

print('введите числа, через пробел.')
print('список 1', end=': ')
str_1 = set(list(map(int, input().split()))[:100000])
print('список 2', end=': ')
str_2 = set(list(map(int, input().split()))[:100000])

print(len(str_1 & str_2))