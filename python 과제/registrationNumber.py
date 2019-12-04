# 2019112801 우예빈
# 주민등록번호 정상 판별 프로그램

class discriminate:
    def inputNumber(self):
        registrationNumber = input("주민등록번호를 숫자만 입력하세요:")
        self.registrationNumber = registrationNumber
    def digits(self):
        if len(self.registrationNumber) == 13:
            alpha = 0
            minus = 0
            space = 0
            for i in (self.registrationNumber):
                if i in "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm":
                    alpha += 1
                elif i == "-":
                    minus += 1
                elif i == " ":
                    space += 1
                if alpha > 0:
                    return "alpha"
                elif minus > 0:
                    return "minus"
                elif space > 0:
                    return "space"
            return 0
        elif len(self.registrationNumber) > 13:
            print("주민등록번호가 13자리 보다 큽니다. 다시 입력하세요.")
            return 1
        else:
            print("입력된 숫자의 자리수가 13자리 이하입니다. 다시 입력하세요.")
            return 1
    def injustice(self):
        number = 11 - ((int(self.registrationNumber[0])*2 + int(self.registrationNumber[1])*3 + int(self.registrationNumber[2])*4 + int(self.registrationNumber[3])*5 + int(self.registrationNumber[4])*6 + int(self.registrationNumber[5])*7 + int(self.registrationNumber[6])*8 +int(self.registrationNumber[7])*9 +int(self.registrationNumber[8])*2 +int(self.registrationNumber[9])*3 +int(self.registrationNumber[10])*4 +int(self.registrationNumber[11])*5)%11)
        if number == 10:
            number = 0
        if number == self.registrationNumber[12]:
            return "right"
        else:
            return "wrong"
a = discriminate()
tf = 1
while (tf == 1):
    a.inputNumber()
    check = a.digits()
    if check == "alpha":
        print("알파벳 문자가 포함되었습니다 다시 입력하세요.")
    elif check == "minus":
        print("-를 빼고 다시 입력하세요.")
    elif check == "space":
        print("공백 문자가 포함되었습니다. 다시 입력하세요.")
    else:
        tf = check

injustice = a.injustice()
if injustice == "wrong":
    print("불법 생성된 주민등록번호입니다.")
else:
    print("정상적인 주민등록번호입니다.")
    age = 20 + (100 - (int(a.registrationNumber[0])*10 + int(a.registrationNumber[1])))>20
    if age >= 20:
        print("성인 인증이 되었습니다. 나이{0}세".format(age))
    print("주민등록번호: {0}".format(a.registrationNumber))
    print("생년월일: {0}".format(a.registrationNumber[0:6]))
    birthAreaNumber = (a.registrationNumber)%1000000
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
    print("출생지:",birthArea)

        
