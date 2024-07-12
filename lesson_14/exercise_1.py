# lesson_14 exercise 1 https://lms.synergy.ru/practicums/attempt/5026001/1?groupPeriodId=1166613

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def printr_list_recursive(l:list):
  length:int = len(l)
  if length > 0:
    print(l[0])
    printr_list_recursive(l[1:])
  else: print('Конец списка')

printr_list_recursive(my_list)