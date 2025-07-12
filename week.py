# 当前日期，需要计算当前是一年的第几周。按照特定的ISO标准？
today = "20250703"
year = 2025
month = 7
day = 3
days_2025 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_total = 0
for day_num in days_2025[:month-1]:
    days_total += day_num

# 截止当前日期，全年的天数。
days_total += day

days_firstweek_2025 = 5

# 计算除去第一周，当前日期是第几周。
week = (days_total - days_firstweek_2025)//7 + 2

print(week)
