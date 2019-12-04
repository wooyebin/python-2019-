# 2019112801 우예빈
# randominlist 클래스 구현

import random


class RandomIntList(list):
    def __init__(self, start, end):
        self.rlist = list()
        for i in range(start, end+1):
            self.rlist.append(random.randint(start, end))
        
    def replace(self, old, new):
        number = 0
        for i in range(len(self.rlist)):
            if self.rlist[i] == old:
                self.rlist[i] = new
                number += 1
        print("{0} 개의 {1}가 {2}로 교체되었습니다.".format(number, old, new))
    def dremove(self):
        for i in range(len(self.rlist)):
            for j in range(i, len(self.rlist)):
                if self.rlist[i] == self.rlist[j]:
                    if i != j:
                        self.rlist[j] = "x"
        for i in self.rlist:
            if "x" in self.rlist:
                self.rlist.remove("x")
        
    def removeall(self, x):
        number = 0
        for i in self.rlist:
            if i == x:
                self.rlist.remove(x)
                number += 1
        print("{0}를 {1}개 삭제하였습니다.".format(x, number))
    def __repr__(self):
        txt1 = ""
        for i in range(len(self.rlist)):
            txt1 += "[%2d]" %i
        txt2 = "["
        for i in range(len(self.rlist)):
            if i != len(self.rlist)-1:
                txt2 += "%3d," %self.rlist[i]
            else:
                txt2 += "%3d" %self.rlist[i]
        txt2+=" ]"
        return '''{0}
{1}'''.format(txt1, txt2)

point = input("RandomIntList 생성(시작과 끝을 입력하세요):")
for i in range(len(point)):
    if point[i] == " ":
        stop = i
startPoint = int(point[0:stop])
endPoint = int(point[stop+1:len(point)+1])
a1 = RandomIntList(startPoint, endPoint)
print(a1)
cont = 0
while cont != 5:
    print('''RandomIntList 테스트
 1. 리스트 출력
 2. replace(old, new)
 3. dremove(): 중복 item 제거
 4. removeall(x): 모든 x 삭제
 5. 종료''')
    cont = int(input("메뉴를 선택하세요:"))
    if cont == 1:
        print(a1.rlist)
    if cont == 2:
        point2 = input("교체할 숫자 (old, new) 입력(공백 구분):")
        for i in range(len(point2)):
            if point2[i] == " ":
                stop2 = i
        old = int(point2[0:stop2])
        new = int(point2[stop2+1:len(point2)+1])
        a1.replace(old, new)
        print(a1)
    if cont == 3:
        a1.dremove()
        print(a1)
    if cont == 4:
        x = int(input("삭제할 숫자를 입력하세요:"))
        a1.removeall(x)
        print(a1)
