# 2019112801 우예빈
# 가장 추웠던 달과 가장 더웠던 달

import csv

f= open('daegu.csv', 'r', encoding = 'euc_kr')
data = csv.reader(f)
header = next(data)

summer6 = []
summer7 = []
summer8 = []
summer9 = []
winter12 = []
winter1 = []
winter2 = []

for row in data:
    year = int(row[0][0:4])
    if (year>=1970)and(year<=2018):
        if row[0][6] == ".":
            month = int(row[0][5])
        else:
            month = int(row[0][5:7])
        if (month>=6)and(month<=9):
            temp = row[-1]
        else:
            temp = row[-2]
        if temp != "":
            if month==6:
                summer6.append(float(temp))
            elif month==7:
                summer7.append(float(temp))
            elif month==8:
                summer8.append(float(temp))
            elif month==9:
                summer9.append(float(temp))       
            elif month==12:
                winter12.append(float(temp))
            elif month==1:
                winter1.append(float(temp))
            elif month==2:
                winter2.append(float(temp))


avgTemp6 = round(sum(summer6)/len(summer6),2)
avgTemp7 = round(sum(summer7)/len(summer7),2)
avgTemp8 = round(sum(summer8)/len(summer8),2)
avgTemp9 = round(sum(summer9)/len(summer9),2)
avgTemp12 = round(sum(winter12)/len(winter12),2)
avgTemp1 = round(sum(winter1)/len(winter1),2)
avgTemp2 = round(sum(winter2)/len(winter2),2)

tempSummer = {"6":avgTemp6, "7":avgTemp7, "8":avgTemp8, "9":avgTemp9}
tempWinter = {"12":avgTemp12, "1":avgTemp1, "2":avgTemp2}

month_max_summer = max(tempSummer.keys(), key=(lambda k:tempSummer[k]))
temp_max_summer = tempSummer[month_max_summer]
month_min_winter = min(tempWinter.keys(), key=(lambda k:tempWinter[k]))
temp_min_winter = tempWinter[month_min_winter]

print('''여름철 평균 기온:
6월 평균기온: {0}도
7월 평균기온: {1}도
8월 평균기온: {2}도
9월 평균기온: {3}도
대구에서 가장 더운 달은 {4}월이고, 평균기온은 {5}도 였습니다.'''.format(avgTemp6,avgTemp7,avgTemp8,avgTemp9,month_max_summer,temp_max_summer))
print()
print('''겨울철 평균 기온:
12월 평균기온: {0}도
1월 평균기온: {1}도
2월 평균기온: {2}도
대구에서 가장 추운 달은 {3}월이고, 평균기온은 {4}도 였습니다.'''.format(avgTemp12,avgTemp1,avgTemp2,month_min_winter,temp_min_winter))
