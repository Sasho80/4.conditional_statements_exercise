starting_number_points = int(input())
bonus_points = 0

if starting_number_points <= 100 and starting_number_points % 2 == 0:
    bonus_points = 5+1
    starting_number_points = starting_number_points+bonus_points
elif starting_number_points <= 100 and starting_number_points % 2 != 0 and starting_number_points % 10 != 5:
    bonus_points = 5
    starting_number_points = starting_number_points + bonus_points
elif starting_number_points <= 100 and starting_number_points % 10 == 5:
        bonus_points = 5+2
        starting_number_points = starting_number_points + bonus_points
elif (100 < starting_number_points < 1001) and starting_number_points % 2 == 0:
        bonus_points = (starting_number_points*0.2)+1
        starting_number_points = starting_number_points + bonus_points
elif (100 <starting_number_points < 1001) and starting_number_points % 2 != 0 and \
        starting_number_points % 10 != 5:
        bonus_points = (starting_number_points * 0.2)
        starting_number_points = starting_number_points + bonus_points
elif (100 < starting_number_points < 1001) and starting_number_points % 10 == 5:
        bonus_points = (starting_number_points * 0.2)+2
        starting_number_points = starting_number_points + bonus_points
elif starting_number_points > 1000 and starting_number_points % 2 == 0:
            bonus_points = (starting_number_points*0.1)+1
            starting_number_points = starting_number_points + bonus_points
elif starting_number_points > 1000 and starting_number_points % 2 != 0 and starting_number_points % 10 != 5:
            bonus_points = (starting_number_points * 0.1)
            starting_number_points = starting_number_points + bonus_points
elif starting_number_points > 1000 and starting_number_points % 10 == 5:
            bonus_points = (starting_number_points * 0.1) + 2
            starting_number_points = starting_number_points + bonus_points
print(bonus_points)
print(starting_number_points)



