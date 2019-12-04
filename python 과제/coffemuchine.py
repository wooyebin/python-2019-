# 2019112801 우예빈
# 커피자판기

def start():
    print('''----------------------------
       커피 자판기 (300원)
1. 블랙커피
2. 프림커피
3. 설탕 프림 커피
4. 재고현황
5. 종료''')

def end():
    print('''---------------------
커피 자판기 동작을 종료합니다.
---------------------''')

def select():
    global i
    if (coin<300):
        i = 0
        print("잔돈이 부족해서 종료합니다.")
        end()
    else:
        start()
        inputNumber = int(input("메뉴를 선택하세요:"))
        if inputNumber == 1:
            black()
        elif inputNumber == 2:
            prim()
        elif inputNumber == 3:
            sugarprim()
        elif inputNumber == 4:
            left()
        else:
            i = 0
            end()

def black():
    global coinCoffe
    global waterCoffe
    global coffeCoffe
    global primCoffe
    global sugarCoffe
    global cupCoffe
    global coin
    global i
    coinCoffe += 300
    coin -= 300
    coffeCoffe -= 30
    waterCoffe -= 100
    cupCoffe -= 1
    if (waterCoffe<0):
        i = 0
        print("물 잔고가 부족해서 종료합니다.")
        end()
    elif (coffeCoffe<0):
        i = 0
        print("커파 잔고가 부족해서 종료합니다.")
        end()
    elif (primCoffe<0):
        i = 0
        print("프림 잔고가 부족해서 종료합니다.")
        end()
    elif (sugarCoffe<0):
        i = 0
        print("설탕 잔고가 부족해서 종료합니다.")
        end()
    elif (cupCoffe<0):
        i = 0
        print("종이컵 잔고가 부족해서 종료합니다.")
        end()
    else:
        print("블랙 커피를 선택하셨습니다. 잔돈: {0}".format(coin))
        select()

def prim():
    global coinCoffe
    global waterCoffe
    global coffeCoffe
    global primCoffe
    global sugarCoffe
    global cupCoffe
    global coin
    global i
    coinCoffe += 300
    coin-=300
    coffeCoffe -= 15
    primCoffe -= 15
    waterCoffe -= 100
    cupCoffe -= 1
    if (waterCoffe<0):
        i = 0
        print("물 잔고가 부족해서 종료합니다.")
        end()
    elif (coffeCoffe<0):
        i = 0
        print("커파 잔고가 부족해서 종료합니다.")
        end()
    elif (primCoffe<0):
        i = 0
        print("프림 잔고가 부족해서 종료합니다.")
        end()
    elif (sugarCoffe<0):
        i = 0
        print("설탕 잔고가 부족해서 종료합니다.")
        end()
    elif (cupCoffe<0):
        i = 0
        print("종이컵 잔고가 부족해서 종료합니다.")
        end()
    else:
        print("프림 커피를 선택하셨습니다. 잔돈: {0}".format(coin))
        select()
        

def sugarprim():
    global coinCoffe
    global waterCoffe
    global coffeCoffe
    global primCoffe
    global sugarCoffe
    global cupCoffe
    global coin
    global i
    coinCoffe += 300
    coin -= 300
    coffeCoffe -= 30
    primCoffe -= 10
    sugarCoffe -= 10
    waterCoffe -= 100
    cupCoffe -= 1
    if (waterCoffe<0):
        i = 0
        print("물 잔고가 부족해서 종료합니다.")
        end()
    elif (coffeCoffe<0):
        i = 0
        print("커파 잔고가 부족해서 종료합니다.")
        end()
    elif (primCoffe<0):
        i = 0
        print("프림 잔고가 부족해서 종료합니다.")
        end()
    elif (sugarCoffe<0):
        i = 0
        print("설탕 잔고가 부족해서 종료합니다.")
        end()
    elif (cupCoffe<0):
        i = 0
        print("종이컵 잔고가 부족해서 종료합니다.")
        end()
    else:
        print("설탕 프림 커피를 선택하셨습니다. 잔돈: {0}".format(coin))
        select()
        
def left():
    global coinCoffe
    global waterCoffe
    global coffeCoffe
    global primCoffe
    global sugarCoffe
    global cupCoffe
    global coin
    print('''----------------------------
재고 현황:
커피: {0}g, 프림: {1}g, 설탕: {2}g
물: {3}ml, 종이컵: {4}개
자판기 남은 돈: {5}원, 잔돈 현황: {6}원'''.format(coffeCoffe, primCoffe, sugarCoffe, waterCoffe, cupCoffe, coinCoffe, coin))

coin = int(input("동전을 투입하세요:"))
coinCoffe = 10000
waterCoffe = 1000
coffeCoffe = 500
primCoffe = 500
sugarCoffe = 500
cupCoffe = 30

i = 1
while i == 1:
    if coin < 300:
        print("돈이 부족합니다. {0}원".format(coin))
        i = 0
        end()
    else:
        select()

