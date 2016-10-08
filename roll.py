import numpy


class Roll(object):
    def StandardRoll(player, value):
        
        weight = 4
        deviation = 1
        roll = round(numpy.random.normal(weight, deviation), 0)
        if roll > 6:
            roll = 6
        elif roll < 0:
            roll = 0
        