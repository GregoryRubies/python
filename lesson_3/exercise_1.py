# exercise 1

def insert_pets(file_name = "pets_list.txt")->str:
  print("Ввести данные питомца:".ljust(100, " "))
  print("вид ", end='')
  pet_type = input()
  print("кличка ", end='')
  pet_name = input()
  print("возраст (лет) ", end='')
  pet_old = input()
  print("записать в хранилище (да/нет)? ", end='')
  if(input() == 'да'):
    pet = (pet_type, pet_name, pet_old)
    pets_list_write = open(file_name, "a", encoding='utf-8')
    pets_list_write.write(", ".join(pet) + '; ')
    pets_list_write.close()
  return f'Это {pet_type} по кличке "{pet_name}". Возраст: {pet_old} года.'

print(insert_pets())