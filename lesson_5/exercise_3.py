# lesson_5 exercise 1 https://lms.synergy.ru/practicums/attempt/5025985/?groupPeriodId=1166613

print('Введите целое число!')
i = int(input())
if i == 0:        print('нулевое число')
elif i % 2 == 1:  print('число не является четным')
elif i < 0:       print('отрицательное четное число')
else:             print('положительное четное число')
