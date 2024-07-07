# lesson_9 exercise 3 https://lms.synergy.ru/practicums/attempt/5025993/1?groupPeriodId=1166613

check_set = set()

print('введите числа, через пробел.', end=': ')

for i in list(map(int, input().split())):
  if i in check_set: 
    print('YES')
  else:
    print('NO')
    check_set.add(i)