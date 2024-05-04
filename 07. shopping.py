#7. Пазаруване
#Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
# Важат следните цени:
#•	Видеокарта – 250 лв./бр.
#•	Процесор – 35% от цената на закупените видеокарти/бр.
#•	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Вход
# Входът се състои от четири реда:
# 1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [1…100]
# 3.	Броят процесори - цяло число в интервала [1…100]
# 4.	Броят рам памет - цяло число в интервала [1…100]
# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# •	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# •	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.

VIDEO_CARD = 250
PROCESSOR_DISCOUNT = 0.35
RAM_MEMORY_DISCOUNT = 0.10
TOTAL_SUM_DISCOUNT = 0.15

sum_video_card =0
price_processor = 0
price_ram_memory =0
total_sum = 0

budget = float(input())
num_video_card = int(input())
num_processor = int(input())
num_ram_memory =int(input())

sum_video_card = num_video_card * VIDEO_CARD
price_processor = (PROCESSOR_DISCOUNT * sum_video_card)*num_processor
price_ram_memory = (RAM_MEMORY_DISCOUNT * sum_video_card)* num_ram_memory

total_sum =sum_video_card + price_processor + price_ram_memory

if num_video_card > num_processor:
    total_sum = total_sum- TOTAL_SUM_DISCOUNT*total_sum

if total_sum > budget:
    print(f"Not enough money! You need {total_sum-budget:.2f} leva more!")
else:
    print(f"You have {budget-total_sum:.2f} leva left!")



