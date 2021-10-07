count_hollidays = int(input()) # почивни дни
play_working_day = 63 #min
play_holiday_day = 127 #min
playing_hours_per_year = 30000 #min

count_working_days = 365 - count_hollidays # работни дни
total_hours_working_day = count_working_days * 63
total_hours_holidays = count_hollidays * 127
total_hours_year = total_hours_holidays + total_hours_working_day

if total_hours_year > 30000:
    print("Tom will run away")
    difference_min = total_hours_year - 30000
    difference_hours = difference_min // 60
    difference_minutes = difference_min % 60
    print(f"{difference_hours} hours and {difference_minutes} minutes more for play")
elif total_hours_year <= 30000:
    print("Tom sleeps well")
    difference = 30000 - total_hours_year
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours} hours and {minutes} minutes less for play")