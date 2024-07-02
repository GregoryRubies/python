# lesson_8 exercise 3 https://lms.synergy.ru/practicums/attempt/5025991/1?groupPeriodId=1166613

def set_condition()->tuple:

  print('Введите грузоподъёмность лоодки, от 1 до 10e6', end=': ')
  m:int = int(input())
  if m > 1000000: 
    raise Exception(f'Грузоподъёмность не должна быть меньше 1 и превышать 10e6. Вы ввели {m}')

  print('Введите кол-во человек, от 1 до 100', end=': ')
  n:int = int(input())
  if n < 1 or n > 100: 
    raise Exception(f'кол-во не должно быть меньше 1 и больше 100')

  return (m, n)

def insert_mens(m:int, n:int)->list[int]:
  a:list[int] = []
  v:int
  print(f'Введите вес, не превыщающий {m}:')
  for i in range(n):
    print(i, end=': ')
    v = int(input())
    if v >= 1 and v <= m:
      a.append(v)
    else: 
      raise Exception(f'значение должно быть в диапазоне от 1 до {m}. Вы ввели {v}')
  return a

def count_crossings(m:int, a:list[int])->int:
  l:int = len(a) - 1
  f:int = 0
  if l == f:
    return 1

  i:bool = True
  c:int = 0
  a.sort()

  while i:
    if f == l:
      c += 1
      i = False
    elif a[f] + a[l] <= m:
      c += 1
      f += 1
      l -= 1
      i = f <= l
    else:
      c += 1
      l -= 1
  return c 

def run_crossings()->count_crossings:
  (m, n) = set_condition()
  return count_crossings(m, insert_mens(m, n))

print(run_crossings())
