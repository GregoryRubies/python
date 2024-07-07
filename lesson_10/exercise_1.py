# lesson_10 exercise 1 https://lms.synergy.ru/practicums/attempt/5025995/1?groupPeriodId=1166613

def get_year_postfix(y:int)->str:
  if y in {11, 12, 13, 14} or y%10 in {0, 5, 6, 7, 8, 9}:
    return 'лет'
  elif y%10 in {2, 3, 4}:
    return 'года'
  else:
    return 'год'

def show_pet_info(pet_name:str, pet_type:str, pet_old:int, pet_owner:str)->str:
  return f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_old} {get_year_postfix(pet_old)}. Имя владельца: {pet_owner}'

def insert_pet(pets:dict):
  print("Ввести данные питомца:".ljust(100, " "))
  print("вид ", end='')
  pet_type = input()
  print("кличка ", end='')
  pet_name = input()
  print("возраст (лет) ", end='')
  pet_old = int(input())
  print("имя владельца ", end='')
  pet_owner = input()
  if  pet_name in pets: 
    print('питомец с таким именем уже существует')
  else: 
    pets[pet_name] = {
      "Вид питомца": pet_type,
      "Возраст питомца": pet_old,
      "Имя владельца": pet_owner
    }

pets = {}


print('начать ввод питомцев? (да/нет):')
a = input()
while a == 'да':
  insert_pet(pets)
  print('продолжить ввод питомцев? (да/нет):')
  a = input()

for k, v in pets.items():
  print(show_pet_info(k, v["Вид питомца"], v["Возраст питомца"], v["Имя владельца"]))
