import random

def roll(max):
    r = random.randint(1,max)
    return r

def rollNTimes(n,max):
    rolls = []
    roll_counts = max*[0]
    for i in range (n):
        r = roll(max)
        rolls.append(r)
        roll_counts[r-1] += 1
    return (roll_counts,rolls)

def main(n,max):
    (roll_counts,rolls) = rollNTimes(n,max)
    for i in range(len(roll_counts)):
        count = roll_counts[i]
        ratio = round(count/n,4)
        percentage = ratio*100
        print(f"{i+1}s:",count,"--", "ratio:",f"{percentage}%")

main(10**6,10)