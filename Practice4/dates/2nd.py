from datetime import date, timedelta

print(f"Yesterday, {date.today() - timedelta(days = 1)}")
print(f"Today, {date.today()}")
print(f"Tomorrow, {date.today() + timedelta(days = 1)}")