# lesson_13 exercise 1 https://lms.synergy.ru/practicums/attempt/5025999/1?groupPeriodId=1166613

from random import randint

def get_matrix(h:int = 10, w:int = 10, r:int=100)->list:
  matrix:list = []
  for i in range(0, h):
    matrix.append([])
    for j in range(w):
      matrix[i].append(randint(-r, r))
  return matrix

def calc_matrix(m_1:list, m_2:list)->list:
  matrix:list = []
  h_1:int = len(m_1)
  h_2:int = len(m_2)
  if h_1 == h_2 and h_1 != 0:
    w_1:int = len(m_1[0])
    w_2:int = len(m_2[0])
    if w_1 == w_2 and w_1 != 0:
      for i in range(0, h_1):
        matrix.append([])
        for j in range(0, w_1):
          matrix[i].append(m_1[i][j] + m_2[i][j])
      return matrix
    else: print(f'ширина матриц не совпадает: {w_1} к {w_2}')
  else: print(f'высота матриц не совпадает: {h_1} к {h_2}')
  return None

print('введите высоту первой матрицы', end=': ')
h_1:int = int(input())
print('введите ширину первой матрицы', end=': ')
w_1:int = int(input())
matrix_1:list = get_matrix(h_1, w_1)
print('матрица 1', matrix_1,sep=': ')
print('введите высоту второй матрицы', end=': ')
h_2:int = int(input())
print('введите ширину второй матрицы', end=': ')
w_2:int = int(input())
matrix_2:list = get_matrix(h_2, w_2)
print('матрица 2', matrix_2,sep=': ')

print('сложение', calc_matrix(matrix_1, matrix_2), sep=':\n')
