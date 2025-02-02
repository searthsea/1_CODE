"""
Bulls&Cows_fin_v1.0.py: druhý projekt do Engeto Online Python Akademie

author: Martin Schwarz
email: svarmartin@gmail.com

Bulls and Cows single player game.
"""

import random
from datetime import datetime, timedelta


def generate_secret_number() -> str:
    """
    Generates a 4 digit random number for the player to guess:
    unique numbers only; 0 is never the 1st digit.
    """
    secret_number = [0]
    while secret_number[0] == 0:
        secret_number = random.sample(range(10), 4)

    return "".join(map(str, secret_number))


def check_tip() -> str:
    """
    Prompts player to enter a valid 4 digit number.
    Checks validity of the tip. Loops until a valid tip is entered.
    Returns a valid player's tip.
    """
    while True:
        tip = input("Enter a number: ")

        if len(tip) != 4:
            print("Number must be exactly 4 digits long!")
            continue
        if not tip.isdigit():
            print("Enter only numbers!")
            continue
        if tip[0] == "0":
            print("Number can't begin with zero!")
            continue
        if len(set(tip)) != 4:
            print("All digits must be unique!")
            continue

        return tip


def assess_tip(secret_number: str, tip: str) -> list:
    """
    Evaluates a player's tip and returns list
    of bulls and cows respectively.
    """
    bulls = 0
    cows = 0
    for index, number in enumerate(secret_number):
        if number == tip[index]:
            bulls += 1
        elif number in tip:
            cows += 1
    return [bulls, cows]


def format_tip(bulls_cows_count: list) -> str:
    """
    Formats player's tip to the correct grammatical number.
    """

    def assign_gramnum(count: int, singular: str, plural: str) -> str:
        return f"{count} {singular if count == 1 else plural}"

    bulls, cows = bulls_cows_count
    return f"{assign_gramnum(bulls, 'bull', 'bulls')}, {assign_gramnum(cows, 'cow', 'cows')}"


def format_totaltime(duration: timedelta) -> str:
    """
    Filters duration of the game to output only the relevant time measures:
    hours, minutes, seconds.
    Formats time to the correct grammatical number and returns it.
    """
    total_sec = int(duration.total_seconds())
    hours, remainder = divmod(total_sec, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_str = ""
    if hours > 0:
        time_str += f"{hours} hours " if hours > 1 else f"{hours} hour "
    if minutes > 0:
        time_str += f"{minutes} minutes " if minutes > 1 else f"{minutes} minute "
    if seconds > 0:
        time_str += f"{seconds} seconds" if seconds > 1 else f"{seconds} second"

    return time_str.strip()


game_intro = """
Welcome to the Bulls & Cows game!\n\
-----------------------------------------------------\n\
RULES:\n\
Guess a random 4 digit number I've generated for you.\n\
If you guess a correct digit in the correct position,\n\
it is called a 'bull', while if you match a digit but\n\
in the wrong position, it is called a 'cow'.\n\
\n\
If you get 4 bulls, wou WIN!\n\
\n\
The secret 4 digit number follows these rules:\n\
- doesn't start with a 0,\n\
- only includes unique digits.\n\
\n\
OK, let's play :)
"""

if __name__ == "__main__":

    secret_number = generate_secret_number()
    print(game_intro)
    count_rounds = 0
    time_start = datetime.now()

    while True:
        print("-----------------------------")
        bulls_cows = assess_tip(secret_number, check_tip())
        count_rounds += 1
        if bulls_cows[0] == 4:
            time_end = datetime.now()
            duration = time_end - time_start
            break
        print(format_tip(bulls_cows))
    print(
        f"""
BINGO! You've won in {count_rounds} rounds!\n\
-----------------------------------------------------\n\
Game completed in:\n\
{format_totaltime(duration)}
"""
    )
