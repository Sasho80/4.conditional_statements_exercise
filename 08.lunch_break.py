# 8. Обедна почивка
# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно
# време да изгледате епизода. По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
# Изход
# На конзолата да се изпише един ред:
# •	Ако времето е достатъчно да изгледате епизода:
#"You have enoug  time to watch {име на сериал} and left with {останало време} minutes free time."
#•	Ако времето не Ви е достатъчно:
#"You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето да се закръгли до най-близкото цяло число нагоре.

from math import ceil
name_series = str(input())
duration_episod = int(input())
duration_break = int(input())

left_time = 0

time_to_lunch = duration_break/8
leiser_time = duration_break/4

duration_break -= time_to_lunch + leiser_time

left_time = abs(duration_break - duration_episod)
left_time = ceil(left_time)

if duration_break >=duration_episod:
    print(f"You have enough time to watch {name_series} and left with {left_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {left_time} more minutes.")


