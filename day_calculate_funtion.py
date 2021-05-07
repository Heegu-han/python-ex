input_year=int(input("연도를 입력하시오."))
input_month=int(input("월을 입력하시오."))
input_day=int(input("일을 입력하시오."))

total_days=0

for year in range(1,input_year):
    if year % 4==0:
        if year % 100==0:
            if year%400==0:
                total_days=total_days+366
            else:
                total_days=total_days+365
        else:
            total_days=total_days+366
    else:
        total_days=total_days+365

days_of_month=[0, 31,28,31,30,31,30,31,31,30,31,30,31]

for month in range(1,input_month):
    total_days=total_days+days_of_month[month]
    
if month >= 3:
    if input_year%4==0:
        if input_year%100==0:
            if input_year%400==0:
                total_days=total_days+1
            else:
                pass
        else:
            total_days=total_days+1
    else:
        pass
total_days=total_days+input_day

result=total_days%7

day_of_week=["일요일","월요일","화요일","수요일","목요일","금요일","토요일"]

print(day_of_week[result])
