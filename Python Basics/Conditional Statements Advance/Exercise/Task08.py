hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())

total_time_of_exam = (hour_of_exam * 60) + minutes_of_exam
total_time_of_arriving = (hour_of_arriving * 60) + minutes_of_arriving

if total_time_of_arriving > total_time_of_exam:
    time_exam_diff = total_time_of_arriving - total_time_of_exam
    if time_exam_diff < 60:
        print("Late")
        print(f"{time_exam_diff} minutes after the start")
    elif time_exam_diff >= 60:
        print("Late")
        hours = time_exam_diff // 60
        minutes = time_exam_diff % 60
        print(f"{hours}:{minutes:0>2d} hours after the start")
elif total_time_of_exam >= total_time_of_arriving:
    time_exam_diff = total_time_of_exam - total_time_of_arriving
    if time_exam_diff == 0:
        print("On time")
    elif time_exam_diff <= 30:
        print("On time")
        print(f"{time_exam_diff} minutes before the start")
    elif 30 < time_exam_diff < 60:
        print("Early")
        print(f"{time_exam_diff} minutes before the start")
    elif time_exam_diff >= 60:
        print("Early")
        hours = time_exam_diff // 60
        minutes = time_exam_diff % 60
        print(f"{hours}:{minutes:0>2d} hours before the start")

