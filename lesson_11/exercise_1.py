# lesson_11 exercise 1 https://lms.synergy.ru/practicums/attempt/5025997/1?groupPeriodId=1166613

def factorial(i:int, m:object = {1: 1})->int:
  if i not in m: 
    m[i] = factorial(i-1, m) * i
  return m[i]

factorial_memo:object = {1: 1}

print(*[factorial(i, factorial_memo) for i in range(1, factorial(int(input()), factorial_memo)+1)][::-1], sep=', ')