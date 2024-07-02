# lesson_8 exercise 2 https://lms.synergy.ru/practicums/attempt/5025991/1?groupPeriodId=1166613

print('введите число N, от 1 до 100000', end=': ')
n =  int(input())
print('N чисел через пробел, от 1 до 100000', end=': ')
a = input().split(' ')

def new_method(a:list, n:int):
  if 1 > n or n > 100000:
    print('первое число должно быть от 1 до 100000')
    return []
  elif len(a) < n:
    print('кол-во введенных элементов меньше N')
    return []
  else:
    b = a[1:n]
    b.append(a[0])
    for v in b:
      e = int(v)
      if 1 > e or e > 1000000000:
        print(f'элемент {e} вне диапазона чисел')
        return []
  return b

print(*new_method(a, n))