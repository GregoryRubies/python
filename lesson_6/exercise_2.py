# lesson_6 exercise 2 https://lms.synergy.ru/practicums/attempt/5025987/?groupPeriodId=1166613

print('Введите число от 1 до 2e9')
x = int(input())
i = 1
c = 0
if x <= 2000000000:
  while i <= x:
    if(x % i  == 0): c += 1
    i += 1
  print(f'количество натуральных делителей числа {x} равно - {c}')
else: print(f'{x} больше 2e9')