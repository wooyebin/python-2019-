registrationNumber = int(input("주민등록번호를 (-)를 빼고 입력하세요: "))
birthAreaNumber = registrationNumber%1000000
birthAreaNumber = birthAreaNumber//10000
if (birthAreaNumber >= 0) and (birthAreaNumber <=8):
    birthArea = "서울"
elif birthAreaNumber <=12:
    birthArea = "부산"
elif birthAreaNumber <=15:
    birthArea = "인천"
elif birthAreaNumber <=25:
    birthArea = "경기"
elif birthAreaNumber <=34:
    birthArea = "강원"
elif birthAreaNumber <=47:
    birthArea = "충청"
elif birthAreaNumber <=66:
    birthArea = "전라"
elif birthAreaNumber <=91:
    birthArea = "경상"
elif birthAreaNumber <=95:
    birthArea = "제주"
else:
    birthArea = "오류"

if birthArea != "오류":
    print("출생 지역은",birthArea,"입니다.")
else:
    print("잘못된 주민등록번호입니다.")
