n = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for days in range(1, n + 1):
    patients = int(input())
    if days % 3 == 0:
        if treated_patients >= untreated_patients:
            enough_patients = treated_patients - untreated_patients
        elif untreated_patients > treated_patients:
            not_enough_patients = untreated_patients - treated_patients
            doctors += 1
    if patients <= doctors:
        treated_patients += patients
    elif patients > doctors:
        treated_patients += doctors
        untreated_patients += patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

