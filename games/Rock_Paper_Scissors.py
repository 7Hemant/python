import random


def play():
    user = input(
        " what's your choice? 'r' for rock , 'p' for paper,'s' for scisser :")

    computer = random .choice(['r', 'p', 's'])

    if user == computer:
        return "it\'s a tie"

    if is_win(user, computer):
        return "You won"

    return "You lost"


def is_win(player, opponent):
    # return true if player wins
    print("is_win function")
    if (player == 'r' and opponent == 's') or (player == "s" and opponent == "p") \
            or (player == "p" and opponent == 'r'):
        return True
    else:
        return False


# calling function
print(play())
