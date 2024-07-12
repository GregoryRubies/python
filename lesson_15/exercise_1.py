# lesson_15 exercise 1 https://lms.synergy.ru/practicums/attempt/5026003/1?groupPeriodId=1166613

from classes import Transport

Autobus:Transport = Transport('Renaul Logan', 180, 12)

print(f'Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}')