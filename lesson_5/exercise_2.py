# lesson_5 exercise 2 https://lms.synergy.ru/practicums/attempt/5025985/?groupPeriodId=1166613

print('Введите вклад Майкла:', end='')
A = float(input())
print('Введите вклад Ивана:', end='')
B = float(input())
print('Введите минимальный вклад:', end='')
X = float(input())
R = '0'
if A>=X and B>=X: R = '2'
elif A>=X: R = 'Mike'
elif B>=X: R = 'Ivan'
elif A+B>=X: R = '1'
print(R)