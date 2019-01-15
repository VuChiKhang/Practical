import random

num_length = 6
min_num = 1
max_num = 45


def main():
    num_quick_pick = int(input("How many quick picks: "))
    while num_quick_pick < 0:
        print("Error! Please type again! ")
        num_quick_pick = int(input("How many quick picks: "))

    for i in range (num_quick_pick):
        quick_pick=[]
        for k in range (num_length):
            num=random.randint(min_num, max_num)
            while num in quick_pick:
                num = random.randint(min_num, max_num)
            quick_pick.append(num)
        quick_pick.sort()

        print(" ".join("{:2}".format(num) for num in quick_pick))

main()