deposit = float(input())
months = int(input())
yearly_interest = float(input())

monthly_interest = (deposit * yearly_interest / 100) / 12
total_money = deposit + ( months * monthly_interest)

print(total_money)
