import random
import re

List4D = []
ListToto = []


def drawn4D():
    for i in range(4):
        randomNum = random.randint(0, 9)
        drawn4D = str(randomNum)
        List4D.append(drawn4D)
    return List4D


def drawnToto():
    for i in range(6):
        randomNumToto = random.randint(1, 49)
        if randomNumToto < 10:
            randomNumToto = "0" + str(randomNumToto)
        drawnToto = str(randomNumToto)
        ListToto.append(drawnToto)
    return ListToto


result4D = re.sub(
    r"\s+", "", str(drawn4D()).strip('[]').replace("'", "").replace(",", ""))
totoResult = str(drawnToto()).strip('[]').replace("'", "")

print("\nUsing random module to generate 4D numbers and Toto numbers")
print(f"Your lucky 4D number is {result4D}")
print(f"Your lucky Toto numbers are {totoResult}\n")
