
def poker(hands):
    "Returns winnning hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    "Returns the hand ranking: hand_rank(hand) => ranking"
    ranks = card_ranks(hand)

    if is_straight(hand) and is_flush(hand):    # straight flush
        return 8
    elif kind(4, hand):                         # four of a kind
        return 7
    elif kind(3, hand) and kind(2, hand):       # full house
        return 6
    elif is_flush(hand):                        # flush
        return 5
    elif is_straight(hand):                     # straight
        return 4
    elif kind(3, hand):                         # three of a kind
        return 3
    elif len(kind(2, hand)) == 2:               # two pairs
        return 2
    elif kind(2, hand):                         # one pair
        return 1
    else:
        return 0                                # high card


def kind(n, hand):
    "Returns the rank(s) with n-of-a-kind: kind(n, hand) => [rank_1, ...]"
    ranks = card_ranks(hand)
    ranks_count = [(r, ranks.count(r)) for r in set(ranks)]
    return sorted([r for r, c in ranks_count if c == n], reverse=True)


def is_straight(hand):
    "Determines if a hand is a straight: is_straight(hand) => True/False"
    ranks = card_ranks(hand)
    return ranks[0] - ranks[-1] == 4 and len(set(ranks)) == 5


def is_flush(hand):
    "Determines if a hand is a flush: is_flush(hand) => True/False"
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
    straight_too = "2S 3C 4S 5H AH".split()
    three_kind = "JS JH JC 5C 8D".split()
    two_pair = "TS TH 6S 6C KC".split()
    one_pair = "AH AC 8D 6H 2S".split()
    high_card = "KH JS TC 6H 3D".split()

    assert is_flush(flush) == True
    assert is_flush(full_house) == False

    assert is_straight(straight_flush) == True
    assert is_straight(straight) == True
    assert is_straight(straight_too) == True
    assert is_straight(flush) == False

    assert kind(4, four_kind) == [14]
    assert kind(3, four_kind) == []
    assert kind(3, three_kind) == [11]
    assert kind(2, three_kind) == []
    assert kind(2, two_pair) == [10, 6]
    assert kind(1, two_pair) == [13]
    assert kind(2, one_pair) == [14]
    assert kind(1, one_pair) == [8,6,2]
    assert kind(1, high_card) == [13, 11, 10, 6, 3]
    assert kind(0, high_card) == []

    assert poker([straight_flush, four_kind, full_house]) == straight_flush
    assert poker([flush, straight, three_kind]) == flush
    assert poker([two_pair, one_pair, high_card]) == two_pair
    assert poker([straight, straight_too]) == straight
    assert poker([straight_too, straight]) == straight

