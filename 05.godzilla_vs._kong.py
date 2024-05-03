budget_film = float(input())
number_extras = int(input())
price_clothing_one_extra = float(input())

decor_film = 0.10
sum_decor = 0
amount_clothing = 0
total_sum_movie = 0
budget_left = 0
discount_clothing = 0.10

sum_decor = budget_film * decor_film
amount_clothing = number_extras * price_clothing_one_extra

if number_extras >150:
    amount_clothing = amount_clothing - amount_clothing * discount_clothing

total_sum_movie = amount_clothing + sum_decor
budget_left = abs(budget_film - total_sum_movie)

if total_sum_movie > budget_film:
    print(f"Not enough money!")
    print(f"Wingard needs {budget_left:.2f} leva more.")
elif total_sum_movie <= budget_film:
    print(f"Action!")
    print(f"Wingard starts filming with {budget_left:.2f} leva left.")
