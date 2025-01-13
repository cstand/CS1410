def dice_game(list_of_rolls):
    score = 0
    for roll in list_of_rolls:
        if roll[0] == roll[1]:
            score = 0
            break
        else:
            score += roll[0] + roll[1]
    return score
