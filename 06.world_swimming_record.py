# 6.	Световен рекорд по плуване
# Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
# разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма,
# която изчислява дали се е справил със задачата, като се има предвид, че:
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иван ще се забави,
# в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.
# Вход
# От конзолата се четат 3 реда:
# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
# Изход
# Отпечатването на конзолата зависи от резултата:
# •	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# o	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
# •	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
# o	"No, he failed! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

from math import floor

record_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

ADD_TIME = 12.5
DISTANCE_TO_ADD_TIME =15

distnace_to_add_extra_time=0
distance_to_swim = 0
extra_time= 0
total_time = 0

distance_to_swim = distance_meters * time_seconds
distance_to_add_extra_time = distance_meters / DISTANCE_TO_ADD_TIME
distance_to_add_extra_time = floor(distance_to_add_extra_time)
extra_time =distance_to_add_extra_time * ADD_TIME
total_time = distance_to_swim +extra_time

if total_time >= record_seconds:
    print(f"No, he failed! He was {total_time - record_seconds:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")


