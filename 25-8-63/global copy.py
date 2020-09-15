import random

HEADS = 1
TAILS = 2
TOSSES = 1000

def main():
    H = 0
    T = 0
    for i in range(TOSSES):
        if random.randint(HEADS,TAILS) == HEADS:
            print("HEADS")
            H = H + 1
        else:
            print("TAILS")
            T = T + 1
            
    print("Heads = ",H)
    print("Tails = ",T)
main()