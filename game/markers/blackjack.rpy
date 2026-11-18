## A hand of blackjack at the Golden Hare (the DoL catalog's Tam's-table fork, loc-casino cards.twee,
## and its punters' table). The plan (2026-11-11): a real hand, hit or stand, the cards called in words
## as patter (sign-off decision 5: dealers' calls stay as patter), never a total or a stake figure.
## It moves nothing and gates nothing: the result is only for the line that follows it.
##
## A test walk (renpy.session["vn_picks"]) is dealt a hand with no natural on either side, so the
## plan's one "Stand" always meets the Hit/Stand menu.

init -5 python:
    import random as _mr_random

    MR_RANKS = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "jack", "queen", "king"]
    MR_SUITS = ["spades", "hearts", "diamonds", "clubs"]

    def _mr_value(rank):
        i = MR_RANKS.index(rank)
        return 11 if i == 0 else min(10, i + 1)

    def mr_bj_total(hand):
        t = sum(_mr_value(r) for r, s in hand)
        aces = sum(1 for r, s in hand if r == "ace")
        while t > 21 and aces:
            t -= 10
            aces -= 1
        return t

    def mr_card(c):
        return "the %s of %s" % c

    def mr_bj_deal():
        test = bool(renpy.session.get("vn_picks"))
        while True:
            deck = [(r, s) for s in MR_SUITS for r in MR_RANKS]
            _mr_random.shuffle(deck)
            p, d = [deck.pop(), deck.pop()], [deck.pop(), deck.pop()]
            if not test or (mr_bj_total(p) < 21 and mr_bj_total(d) < 21):
                break
        store.mr_bj = VNState(deck=deck, player=p, dealer=d, result=None)

    def mr_bj_hit():
        c = mr_bj.deck.pop()
        mr_bj.player.append(c)
        return c

    def mr_bj_dealer_play():
        drawn = []
        while mr_bj_total(mr_bj.dealer) < 17:
            c = mr_bj.deck.pop()
            mr_bj.dealer.append(c)
            drawn.append(c)
        return drawn

    def mr_bj_settle():
        p, d = mr_bj_total(mr_bj.player), mr_bj_total(mr_bj.dealer)
        if p > 21:
            r = "lose"
        elif p == 21 and len(mr_bj.player) == 2 and not (d == 21 and len(mr_bj.dealer) == 2):
            r = "natural"
        elif d > 21 or p > d:
            r = "win"
        elif p == d:
            r = "push"
        else:
            r = "lose"
        mr_bj.result = r
        return r

default mr_bj = VNState()

## One hand. `dealer` names who deals (Tam, or the punters' day dealer). Sets mr_bj.result.
label mr_bj_hand(dealer="Tam"):
    $ mr_bj_deal()
    $ _c1, _c2, _up = mr_card(mr_bj.player[0]), mr_card(mr_bj.player[1]), mr_card(mr_bj.dealer[0])
    vn_sfx "Fft. Fft. Fft. Fft."
    "[dealer] deals. You get [_c1] and [_c2]. [dealer] shows [_up]."
    $ _mr_stand = mr_bj_total(mr_bj.player) == 21
    if _mr_stand:
        "A natural, straight off the deal."
    while not _mr_stand:
        menu:
            "Your hand sits on the felt. [dealer] waits."
            "Hit me":
                $ _c = mr_card(mr_bj_hit())
                "[dealer] flicks you [_c]."
                if mr_bj_total(mr_bj.player) > 21:
                    "Bust."
                    $ mr_bj_settle()
                    return
                if mr_bj_total(mr_bj.player) == 21:
                    "Sitting pretty. You stand."
                    $ _mr_stand = True
            "Stand":
                $ _mr_stand = True
    $ _hole = mr_card(mr_bj.dealer[1])
    "[dealer] turns over [_hole]."
    $ _drawn = mr_bj_dealer_play()
    if _drawn:
        $ _drawn_s = " and ".join(mr_card(c) for c in _drawn)
        "And draws [_drawn_s]."
    if mr_bj_total(mr_bj.dealer) > 21:
        "The house busts."
    $ mr_bj_settle()
    return
