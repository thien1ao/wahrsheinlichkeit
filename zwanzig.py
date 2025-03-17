import random

N_ROLLS = 100


def roll():
    return random.randint(1, 6)


def fill():
    roll_dict = {}

    for i in range(N_ROLLS):
        rolled = roll()

        if rolled in roll_dict:
            roll_dict[rolled] += 1
        else:
            roll_dict[rolled] = 1

    return roll_dict


def print_rolls():
    roll_dict = fill()
    for key, value in roll_dict.items():
        print("key: %d, value: %d" % (key, value))
    print("\n")


def calculate_p(roll_dict):
    for key, value in roll_dict.items():
        p = (value / N_ROLLS) * 100
        print(f"key: {key}, p: {p:.2f}%")


roll_dict = fill()
print_rolls()
calculate_p(roll_dict)
