# 2019112801 우예빈
# 에라토스테네스의 체


def prints():
    for i in range(0,10):
        for j in range(0+i*10, 10+i*10):
            if j != 99:
                print(" %2s" %originalNumber[j], end =" ")
        print("")

def printing(number):
    print("Remove {}'s multiple numbers".format(number))
    prints()

def remove(number):
    for i in originalNumber:
        if i != "X":
            if (i != number)and(i%number == 0):
                originalNumber[originalNumber.index(i)] = "X"
    printing(number)

originalNumber = []
for i in range(2,101):
    originalNumber.append(i)

print("Original number =>")
prints()
remove(2)
remove(3)
remove(5)
remove(7)
print("Prime numbers:")
prints()
