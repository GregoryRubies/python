# lesson_6 exercise 3 https://lms.synergy.ru/practicums/attempt/5025987/?groupPeriodId=1166613

print('Введите целые числа A и B, где A ≤ B')

for i in range(int(input()),  int(input())+1):
  if i % 2 == 0:
    print(i, end=' ')