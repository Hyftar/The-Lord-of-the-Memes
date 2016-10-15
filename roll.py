import numpy


class Roll(object):
    def StandardRoll(player, value, rollmin, rollmax):
        weight = 4
        deviation = 1
        roll = round(numpy.random.normal(weight, deviation), 0)
        if roll > rollmax:
            roll = 6
        elif roll < rollmin:
            roll = 0
