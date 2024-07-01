# lesson_4 exercise 1 https://lms.synergy.ru/practicums/attempt/5025983/?groupPeriodId=1166613

print('Введите  целое, пятизначное число:', end=' ')
x = input()
if int(x) > 99999 or int(x) < 10000:
  print(f'число {x} не удовлетворяет условию!')
else:
  a, b, c, d, e = [float(i) for i in x]
  if a != b:
    print(f'{(pow(d, e) * c) / (a - b) }')
  else: print('На ноль делить нельзя')