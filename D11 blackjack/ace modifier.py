import random

ace = [random.randint(1,11), random.randint(1,11), random.randint(1,11)]
tot = sum(ace)
print(ace)
print(tot)

if tot >= 21:
    if 11 in ace:
        conv = ace.index(11)
        print(conv)
        ace[conv] = 1
        print(sum(ace))
        print(tot)
    else:
        print("No")

else:
    print(tot)
