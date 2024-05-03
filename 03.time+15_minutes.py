hours = int(input())
minutes = int(input())

search_hours = 0
search_minutes = 0
next_fifteen_minutes = 15

hours =60*hours # convert hours to minutes
total_time = hours + minutes + next_fifteen_minutes

search_hours = total_time // 60

if search_hours <=23:
    search_hours = total_time // 60
else:
    search_hours = 0

search_minutes = total_time % 60

if search_minutes <= 9:
    print(f"{search_hours}:0{search_minutes}")
else:
    print(f"{search_hours}:{search_minutes}")



