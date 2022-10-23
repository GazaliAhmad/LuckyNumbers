import random
import re

result4D = []
toto = []


def num4D():
    for i in range(4):
        randomNum = random.randint(0, 9)
        num4D = str(randomNum)
        result4D.append(num4D)
    return result4D


res4D = re.sub(
    r"\s+", "", str(num4D()).strip('[]').replace("'", "").replace(",", ""))


def Toto():
    for i in range(6):
        randomNum1 = random.randint(0, 9)
        randomNum2 = random.randint(0, 9)
        while (randomNum1 == 0 and randomNum2 == 0):
            randomNum1 = random.randint(0, 9)
            randomNum2 = random.randint(0, 9)
        randomNum = str(randomNum1) + str(randomNum2)
        toto.append(randomNum)
    return toto


totoRes = str(Toto()).strip('[]').replace("'", "")

print(f"\nYour lucky 4D number is {res4D}")
print(f"Your lucky Toto numbers are {totoRes}\n")
