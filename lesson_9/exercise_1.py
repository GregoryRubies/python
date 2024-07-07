# lesson_9 exercise 1 https://lms.synergy.ru/practicums/attempt/5025993/1?groupPeriodId=1166613

from my_module import scope

scope = scope(20000000000)
    
print('Введите число от 1 до 100000', end=': ')
n =  int(input())
if 1 <= n and n <= 100000:
  print(f'Вводите числа от -20000000000 до 20000000000, {n} раз через пробел:')
  print(len(set(list(map(scope, input().split()))[:n])))
else: print('первое число должно быть от 1 до 100000')