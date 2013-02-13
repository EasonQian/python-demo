# -*- coding: cp936 -*-
# 根据年月日以数字形式打印出日期

months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']

# 以1- 31的数字作为结尾的列表
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + \
          ['st', 'nd', 'rd'] + 7 * ['th'] + \
          ['st']          

year = raw_input("Year: ")
month = raw_input("Month(1-12): ")
day = raw_input("Day(1-31): ")

month_int = int(month)
day_int = int(day)

# 根据输入获得正确的索引
month_str = months[month_int - 1]
day_str = day + endings[day_int - 1];

print month_str + ' ' + day_str + ', ' + year
