import random
talist=[]
for i in range(1000):
    randomnum=random.choices([0,1],k=5)
    if randomnum not in talist:
        talist.append(randomnum)
print(len(talist))
print(talist)