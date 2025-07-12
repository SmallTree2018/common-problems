

# 当前日期，需要计算当前是一年的第几周。按照特定的ISO标准？
from datetime import datetime

today = datetime.today().astimezone()
year = today.year
month = today.month
day = today.day
tz = today.tzinfo

# 使用标准库获取ISO周数
week = today.isocalendar()[1]

print("当前日期是", year, "年", month, "月", day, "日，时区：", tz)
print("今天是第", week, "周")
