# 2019112801 우예빈
# 카드게임
import random

card_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_suit = ["♠", "♥", "♣", "◆"]
card_set = [(i , j) for i in card_suit for j in card_number]

def printing(List = card_set):
    for i in range(4):
        for j in range(13*i,13+13*i):
            print(List[j], end=" ")
        print()

def scoreCal(playerList):
    score = 0
    for i in range(len(playerList)):
        suit = playerList[i][0]
        if suit == "♠":
            scoreSuit=3
        elif suit == "♥":
            scoreSuit=1
        elif suit == "♣":
            scoreSuit= 4
        else:
            scoreSuit=2
        scoreNumber = playerList[i][1]
        score += scoreSuit * scoreNumber
    return score
            

print("초기 카드 생성")
printing()
random.shuffle(card_set)
print("Shuffle Card")
printing()

player1 = [card_set[-1], card_set[-3], card_set[-5]]
player2 = [card_set[-2], card_set[-4], card_set[-6]]
print("Dealing three cards")
print("Player1:  {}".format(player1))
print("Player2:  {}".format(player2))

player1Score = scoreCal(player1)
player2Score = scoreCal(player2)
print("Player1: {0}, Player2: {1}".format(player1Score,player2Score))
if player1Score>player2Score:
    print("Player1 Win")
elif player1Score<player2Score:
    print("Player2 Win")
else:
    print("Draw")
