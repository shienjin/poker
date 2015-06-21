
def poker(hands):
    "Returns winnning hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    "Returns the hand ranking: hand_rank(hand) => ranking"
    return
