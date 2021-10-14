city = input()
sales = float(input())
commision = 0
if city == "Sofia":
    if 0 <= sales <= 500:
        commision = sales * 0.05
    elif 500 < sales <= 1000:
        commision = sales * 0.07
    elif 1000 < sales <= 10000:
        commision = sales * 0.08
    elif sales > 10000:
        commision = sales * 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        commision = sales * 0.045
    elif 500 < sales <= 1000:
        commision = sales * 0.075
    elif 1000 < sales <= 10000:
        commision = sales * 0.1
    elif sales > 10000:
        commision = sales * 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commision = sales * 0.055
    elif 500 < sales <= 1000:
        commision = sales * 0.08
    elif 1000 < sales <= 10000:
        commision = sales * 0.12
    elif sales > 10000:
        commision = sales * 0.145

if commision > 0:
    print("%.2f" % commision)
else:
    print("error")