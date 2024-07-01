# lesson_7 exercise 1 https://lms.synergy.ru/practicums/attempt/5025989/1?groupPeriodId=1166613
from re import sub

s =  input()
if s.__len__() <= 1000:
  print(sub(r'\s+', ' ', s))