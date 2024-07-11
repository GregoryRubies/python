# lesson_11 exercise 2 https://lms.synergy.ru/practicums/attempt/5025997/1?groupPeriodId=1166613

from collections import deque

pets = {
  1: {
    "Мухтар": {
      "Вид питомца": "Собака",
      "Возраст питомца": 9,
      "Имя владельца": "Павел"
    },
  },
  2: {
    "Каа": {
      "Вид питомца": "желторотый питон",
      "Возраст питомца": 19,
      "Имя владельца": "Саша"
    },
  },
}

last = deque(pets, maxlen=1)[0]

def show_pet_info(pet_name:str, pet_type:str, pet_old:int, pet_owner:str)->str:
  return f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_old} {get_suffix(pet_old)}. Имя владельца: {pet_owner}'

def get_pet(id:int, pets:dict = pets)->dict:
  return pets[id] if id in pets.keys() else False

def print_pet_info(pet:dict, id:int)->None:
    pet_name:str = [*pet.keys()][0]
    pet_info:dict = [*pet.values()][0]
    print(id, show_pet_info(pet_name, pet_info["Вид питомца"], pet_info["Возраст питомца"], pet_info["Имя владельца"]), sep=': ')

def get_suffix(age:int)->str:
  if age in {11, 12, 13, 14} or age%10 in {0, 5, 6, 7, 8, 9}:
    return 'лет'
  elif age%10 in {2, 3, 4}:
    return 'года'
  else:
    return 'год'

def pets_list(pets:dict = pets)->None:
  for id, current_pet in pets.items():
    print_pet_info(current_pet, id)

def insert_pet_info()->tuple:
  print("Ввести данные питомца:".ljust(100, " "))
  print("вид ", end='')
  pet_type = input()
  print("кличка ", end='')
  pet_name = input()
  print("возраст (лет) ", end='')
  pet_old = int(input())
  print("имя владельца ", end='')
  pet_owner = input()
  return (pet_type, pet_name, pet_old, pet_owner)

def create(pets:dict = pets, last:int = last)->None:
  pet_type, pet_name, pet_old, pet_owner = insert_pet_info()
  print(show_pet_info(pet_name, pet_type, pet_old, pet_owner), 'Создать запись (yes/no)', sep='\n', end=': ')
  if input() == 'yes':
    last += 1
    pets[last] = {
      pet_name: {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_old,
        "Имя владельца": pet_owner
      }
    }
    print('успешно записано.')
  else: print('запись  отменена.')

def read(id:int, pets:dict = pets)->None:
  print_pet_info(pets[id], id) if id in pets else print('Питомец с таким идентификатором отсутствует в базе')

def update(id:int, pets:dict = pets)->None:
  if id in pets:
    read(id, pets)
    print('хотите обновить информацию? (yes/no)', end=': ')
    if input() == 'yes':
      pet_type, pet_name, pet_old, pet_owner = insert_pet_info()
      print(show_pet_info(pet_name, pet_type, pet_old, pet_owner), 'Обновить запись (yes/no)', sep='\n', end=': ')
      if input() == 'yes':
        pets[id] = {
          pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_old,
            "Имя владельца": pet_owner
          }
        }
        print('успешно обновлено.')
      else: print('обновление отменено.')
    else: print('обновление отменено.')
  else: print('Питомец с таким идентификатором отсутствует в базе')

def delete(id:int, pets:dict = pets)->dict:
  if id in pets:
    read(id, pets)
    print('хотите удалить информацию? (yes/no)', end=': ')
    if input() == 'yes':
      pets.pop(id)
    else: print('удаление отменено.')
  else: print('Питомец с таким идентификатором отсутствует в базе')

def print_comand_list():
  print(
    'список поддерживаемых команд:'
    , 'stop - остановить программу'
    , 'create - добавить питомца'
    , 'read - получить информацию о питомце'
    , 'update - обновить информацию'
    , 'delete - удалить запись'
    , 'list - вывести информацию обо всех питомцах'
    , 'help - список команнд'
    , sep='\n  - '
  )

print_comand_list()
print('введите команду', end=': ')
command:str = input()

while command != 'stop':
  if command == 'create': create()
  elif command == 'read': 
    print('введите числовой идентификатор', end=': ')
    read(int(input()))
  elif command == 'update': 
    print('введите числовой идентификатор', end=': ')
    update(int(input()))
  elif command == 'delete': 
    print('введите числовой идентификатор', end=': ')
    delete(int(input()))
  elif command == 'list': pets_list()
  elif command == 'help': print_comand_list()
  else: print('!команда не распознана!', 'введите help чтобы получить список поддерживаемых команнд', sep='\n')
  print('введите команду', end=': ')
  command = input()

print('Программа завершена.')