# lesson_5 exercise 2 https://lms.synergy.ru/practicums/attempt/5025985/?groupPeriodId=1166613

print('Введите слово!')
word = input()
letter_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
letter_count = 0
for letter in  word:
  if letter in letter_dict:
    letter_dict[letter] += 1

print(f'Количество букв в слове {word}:')
for k, v in letter_dict.items():
  letter_count += v
  print(f'{k}: {v if v != 0 else False}')

print(f'Всего гласных букв: {letter_count}')
print(f'Всего согласных букв: {word.__len__() - letter_count}')