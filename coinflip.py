# coin flip
import random

def flip_coin():
    return 'H' if random.randint(0, 1) == 0 else 'T'

def has_streak(coin_flips, streak_length=6):
    # Check for a streak of specified length in the list of coin flips
    current_streak = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            current_streak += 1
            if current_streak == streak_length:
                return True
        else:
            current_streak = 1
    return False

number_of_streaks = 0
experiments = 10000
flips_per_experiment = 100

for experiment_number in range(experiments):
    # Generate a list of 100 random 'H' or 'T'
    coin_flips = [flip_coin() for _ in range(flips_per_experiment)]
    # Check if there is a streak of 6 heads or tails in a row
    if has_streak(coin_flips):
        number_of_streaks += 1
# Calculate and print the chance of streak
chance_of_streak = (number_of_streaks / experiments) * 100
print('Chance of streak: %s%%' % chance_of_streak)
