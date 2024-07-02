# lesson_8 exercise 1 https://lms.synergy.ru/practicums/attempt/5025991/1?groupPeriodId=1166613

def scope(v:str)->int:
  try:
    n = int(v)
    if -100000 <= n and n <= 100000:
      return n
    else: 
      print('число по модулю не должно превышать 10e5')
  except ValueError: 
    print('вы ввели не число')
    

n =  int(input())
if 1 <= n and n <= 100000:
  print(*(([scope(input()) for i in range(n)])[::-1]))
else: print('первое число должно быть от 1 до 100000')