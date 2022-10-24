import random

List4D = []
ListToto = []

for i in range(10000):
    List4D.append(i)

drawn4D = random.sample(List4D, 1)
for i in range(len(drawn4D)):
    if drawn4D[i] < 10:
        drawn4D[i] = "000" + str(drawn4D[i])
    elif drawn4D[i] < 100:
        drawn4D[i] = "00" + str(drawn4D[i])
    elif drawn4D[i] < 1000:
        drawn4D[i] = "0" + str(drawn4D[i])


for i in range(1, 50):
    ListToto.append(i)

drawnToto = random.sample(ListToto, 6)
for i in range(len(drawnToto)):
    if drawnToto[i] < 10:
        drawnToto[i] = "0" + str(drawnToto[i])
    else:
        drawnToto[i] = str(drawnToto[i])

result4D = str(drawn4D).strip('[]').replace("'", "")
TotoResult = str(drawnToto).strip('[]').replace("'", "")

print("\nRandom choice from a list for 4D numbers (0 to 9999) and Toto numbers (01 to 49)")
print(f"Your lucky 4D number is {result4D}")
print(f"Your lucky Toto numbers are {TotoResult}\n")
