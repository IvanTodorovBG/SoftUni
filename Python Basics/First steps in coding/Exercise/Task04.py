count_sheets = int(input())
sheets_per_hour = int(input())
days = int(input())

hours_for_reading_per_day = (count_sheets / sheets_per_hour ) / days
print(hours_for_reading_per_day)
