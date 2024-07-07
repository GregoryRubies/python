def scope(f:int):
  def inner(v:str)->int:
    try:
      n = int(v)
      if -f <= n and n <= f:
        return n
      else:
        raise Exception(f'число по модулю не должно превышать {f}. Вы ввели {v}')
    except ValueError: 
      print('вы ввели не число')

  return inner
