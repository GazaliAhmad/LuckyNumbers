import random

result4D = []
toto = []

for i in range(10000):
    result4D.append(i)

drawn4D = random.sample(result4D, 1)
for i in range(len(drawn4D)):
    if drawn4D[i] < 10:
        drawn4D[i] = "000" + str(drawn4D[i])
    elif drawn4D[i] < 100:
        drawn4D[i] = "00" + str(drawn4D[i])
    elif drawn4D[i] < 1000:
        drawn4D[i] = "0" + str(drawn4D[i])
drawn4Dresult = str(drawn4D).strip('[]').replace("'", "")


for i in range(1, 49):
    toto.append(i)

drawnToto = random.sample(toto, 6)
for i in range(len(drawnToto)):
    if drawnToto[i] < 10:
        drawnToto[i] = "0" + str(drawnToto[i])
    else:
        drawnToto[i] = str(drawnToto[i])

TotoResult = str(drawnToto).strip('[]').replace("'", "")

print("\nRandom choice from a list for 4D numbers (0 to 9999) and Toto numbers (01 to 49)")
print(f"Your lucky 4D number is {drawn4Dresult}")
print(f"Your lucky Toto numbers are {TotoResult}\n")
