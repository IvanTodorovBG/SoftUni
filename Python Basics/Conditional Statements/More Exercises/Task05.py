needed_hours_for_project = int(input())
days = int(input())
workers = int(input())
import math

days_for_project = days - (days * 0.1)
hours_for_project_workday = days_for_project * 8
hours_for_project_overday = days * 2 * workers
total_hours = hours_for_project_overday + hours_for_project_workday

if total_hours >= needed_hours_for_project:
    extra_time = total_hours - needed_hours_for_project
    print(f"Yes!{math.floor(extra_time)} hours left.")
else:
    not_enough = needed_hours_for_project - total_hours
    print(f"Not enough time!{math.ceil(not_enough)} hours needed.")