# lesson_9 exercise 1 https://lms.synergy.ru/practicums/attempt/5025993/1?groupPeriodId=1166613

def scope(v:str)->int:
  try:
    n = int(v)
    if -2000000000 <= n and n <= 2000000000:
      return n
    else:
      raise Exception(f'число по модулю не должно превышать 2*10e9. Вы ввели {v}')
  except ValueError: 
    print('вы ввели не число')
    
print('Введите число от 1 до 100000', end=': ')
n =  int(input())
if 1 <= n and n <= 100000:
  print(f'Вводите числа от -2000000000 до 2000000000, {n} раз:')
  print(len({scope(input()) for i in range(n)}))
else: print('первое число должно быть от 1 до 100000')