
def poker(hands):
    "Returns winnning hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    "Returns the hand ranking: hand_rank(hand) => ranking"
    return


def card_rank(hand):
    """
    Returns card rankings in reverse sorted order. Note: A = 14 or 1.
    card_rank(hand) => [rank_1, rank_2, ...]
    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks
