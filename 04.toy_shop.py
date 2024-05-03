from math import fabs

excursion_price = float(input())
num_puzzles = int(input())
num_talking_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

puzzel = 2.60
talking_dolls = 3
teddy_bear = 4.10
minions = 8.2
truck = 2
discount =0.25

sum_toys = 0
num_toys = 0
sum_toys_discount = 0
rent_shop = 0
price_rent = 0.10
gain_shop = 0
money_remains = 0

sum_toys = num_puzzles * puzzel + num_talking_dolls * talking_dolls +num_teddy_bears * teddy_bear + \
           num_minions * minions +num_trucks * truck

num_toys = num_puzzles + num_talking_dolls + num_teddy_bears + num_minions + num_trucks

if num_toys >= 50:
    sum_toys_discount = sum_toys*discount

sum_toys =sum_toys-sum_toys_discount
rent_shop = sum_toys * price_rent
gain_shop = sum_toys -rent_shop

money_remains = fabs(gain_shop - excursion_price)
if gain_shop >= excursion_price:
    print(f"Yes! {money_remains:.2f} lv left.")
else:
    print(f"Not enough money! {money_remains:.2f} lv needed.")
