import random

trials = 1000000
offBoard = 0
onBoard = 0

for i in range(trials):
    lCount = 0
    rCount = 0
    curr = [0 for z in range(6)]
    for n in range(6):
        curr[n] = random.getrandbits(1)
            
    for x in range(len(curr)):
        if curr[x]:
            rCount+=1
        else:
            lCount+=1
        
        if rCount == 3 and lCount == 0 or rCount == 0 and lCount == 3:
            offBoard+=1
            break
        elif rCount == 2 and lCount == 2:
            onBoard+=1
            break
        elif rCount == 1 and lCount == 4 or rCount == 4 and lCount == 1:
            offBoard+=1
            break
        elif rCount == 2 and lCount == 4 or rCount == 4 and lCount == 2:
            onBoard+=1
            break
        elif rCount == 3 and lCount == 3:
            onBoard+=1
            break

probabilityOn = onBoard/trials # ~0.56
probabilityOff = offBoard/trials # ~0.44
print("Probability Off: " + str(probabilityOff))
print("Probability On: " + str(probabilityOn))
