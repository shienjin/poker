
def poker(hands):
    "Returns winnning hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    "Returns the hand ranking: hand_rank(hand) => ranking"
    ranks = card_ranks(hand)
    return


def is_flush(hand):
    "Determine if a hand is a flush: flush(suits) => True/False"
    suits = [s for _, s in hand]
    return len(set(suits)) == 1


def card_ranks(hand):
    """
    Returns card rankings in reverse sorted order. Note: A = 14 or 1.
    card_ranks(hand) => [rank_1, rank_2, ...]
    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks


def tests():
    "Test cases"
    straight_flush = "5C 6C 7C 8C 9C".split()
    four_kind = "AD AS AC AH 8C".split()
    full_house = "KH KC KS TH TC".split()
    flush = "QC 6C 4C 3C 8C".split()
    straight = "2S 3C 4S 5H 6H".split()
    three_kind = "JS JH JC 5C 8D".split()
    two_pair = "10S 10H 6S 6C KC".split()
    one_pair = "AH AC 8D 6H 2S".split()
    high_card = "KH JS 10C 6H 3D".split()

    assert is_flush(flush) == True
    assert is_flush(full_house) == False

    assert poker([straight_flush, four_kind, full_house]) == straight_flush
    assert poker([flush, straight, three_kind]) == flush
    assert poker([two_pair, one_pair, high_card]) == two_pair
