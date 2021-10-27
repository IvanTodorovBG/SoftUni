n = int(input())
salary = int(input())

Facebook = 150
Instagram = 100
Reddit = 50


for i in range(n):
    numbers = input()
    if numbers == "Facebook":
        salary -= Facebook
    if numbers == "Instagram":
        salary -= Instagram
    if numbers == "Reddit":
        salary -= Reddit
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
