class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50

    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE

    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR

    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * FIVE

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX

    @staticmethod
    def pair(*dice):
        PAIR = 2
        for numero in range(6, 0, -1):
            if dice.count(numero) >= PAIR:
                return PAIR * numero
        return 0

    @staticmethod
    def two_pairs(*dice):
        PAIR = 2
        pairs = 0
        score = 0
        numero = 1
        while pairs < 2 and numero <= 6:
            if dice.count(numero) >= 2:
                pairs += 1
                score += PAIR * numero
            numero += 1
        if pairs == 2:
            return score
        else:
            return 0

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        for numero in range(6, 0, -1):
            if dice.count(numero) >= THREE:
                return THREE * numero
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        for numero in range(6, 0, -1):
            if dice.count(numero) >= FOUR:
                return FOUR * numero
        return 0

    @staticmethod
    def small_straight(*dice):
        for numero in range(1, 6):
            if dice.count(numero) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def large_straight(*dice):
        for numero in range(2, 7):
            if dice.count(numero) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.__par_bajo(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy.__par_bajo(*dice) + Yatzy.three_of_a_kind(*dice)
        else:
            return 0

    @staticmethod
    def __par_bajo(*dice):
        PAIR = 2
        for numero in range(6, 0, -1):
            if dice.count(numero) == PAIR:
                return PAIR * numero
        return 0
