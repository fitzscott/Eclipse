# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:19:28 2017

@author: bushnelf
"""

import random


class DiceRoller:
    """
    DiceRoller - for six-sided dice, take a number of dice to roll,
    a to-hit number, and determine how many hits will occur per roll,
    average.  Also report how many rolls will be required to yield
    a certain number of hits.
    """

    def __init__(self, tohit, reqdhits=0):
        self._tohit = tohit
        self._reqdhits = reqdhits
        self._sides = 6
        self._rollcount = 1000000
        # self._rollcount = 10
        random.seed()

    @property
    def tohit(self):
        return(self._tohit)

    @tohit.setter
    def tohit(self, num):
        self._tohit = num

    @property
    def reqdhits(self):
        return(self._reqdhits)

    @reqdhits.setter
    def reqdhits(self, num):
        self._reqdhits = num

    def roll(self, count):
        """
        roll - roll count dice, compare against the tohit number,
        and return the hit percentage.
        """
        numhits = 0
        diedist = [0, 0, 0, 0, 0, 0]

        for d in range(count):
            rol = random.randint(1, self._sides)
            diedist[rol - 1] += 1
            if rol >= self.tohit:       # self._tohit:
                numhits += 1
        # print(str(diedist))
        return(numhits * 1.00 / (count * 1.00))

    def roundstoachieve(self, numdice, numhitsperdie=1):
        avghits = self.roll(self._rollcount) * numdice * numhitsperdie
        roundsreqd = self._reqdhits * 1.00 / avghits
        # print("Rounds required is " + str(roundsreqd))
        print(str(self.reqdhits) + " hit(s) with a " + str(self.tohit) +
              " to hit requires " + str(round(roundsreqd, 2)) + " rounds.")
        return(roundsreqd)

if __name__ == "__main__":
    print("*** Ancient attacking!")
    print("          Interceptor w/ 1 hull:")
    dc = DiceRoller(5, 2)
    rr = dc.roundstoachieve(2)
    print("           Interceptor w/ gauss shield")
    dc2 = DiceRoller(6, 1)
    rr = dc2.roundstoachieve(2)

    print("          Cruiser w/ 2 hull:")
    dc = DiceRoller(5, 3)
    rr = dc.roundstoachieve(2)
    print("          Cruiser w/ 1 hull + gauss shield:")
    dc2 = DiceRoller(6, 2)
    rr = dc2.roundstoachieve(2)

    print("          Dreadnaught w/ 6 hull:")
    dc = DiceRoller(5, 7)
    rr = dc.roundstoachieve(2)
    print("          Dreadnaught w/ 4 hull + gauss shield:")
    dc2 = DiceRoller(6, 5)
    rr = dc2.roundstoachieve(2)
    print("          Dreadnaught w/ 2 hull + 2 gauss shield (bad):")
    dc = DiceRoller(6, 3)
    rr = dc.roundstoachieve(2)

    print("*** Cruiser w/ 2 plasma cannon + electron computer attacking!")
    print("          Interceptor w/ 1 hull:")
    dc = DiceRoller(5, 2)
    rr = dc.roundstoachieve(2, 2)
    print("           Interceptor w/ gauss shield")
    dc2 = DiceRoller(6, 1)
    rr = dc2.roundstoachieve(2, 2)

    print("          Cruiser w/ 2 hull:")
    dc = DiceRoller(5, 3)
    rr = dc.roundstoachieve(2, 2)
    print("          Cruiser w/ 1 hull + gauss shield:")
    dc2 = DiceRoller(6, 2)
    rr = dc2.roundstoachieve(2, 2)

    print("          Dreadnaught w/ 6 hull:")
    dc = DiceRoller(5, 7)
    rr = dc.roundstoachieve(2, 2)
    print("          Dreadnaught w/ 4 hull + gauss shield:")
    dc2 = DiceRoller(6, 5)
    rr = dc2.roundstoachieve(2, 2)
    print("          Dreadnaught w/ 2 hull + 2 gauss shield (bad):")
    dc = DiceRoller(6, 3)
    rr = dc.roundstoachieve(2, 2)

    print("*** Cruiser w/ 2 ion cannon + positron computer attacking!")
    print("          Interceptor w/ 1 hull:")
    dc = DiceRoller(4, 2)
    rr = dc.roundstoachieve(2)
    print("           Interceptor w/ gauss shield")
    dc2 = DiceRoller(5, 1)
    rr = dc2.roundstoachieve(2)

    print("          Cruiser w/ 2 hull:")
    dc = DiceRoller(4, 3)
    rr = dc.roundstoachieve(2)
    print("          Cruiser w/ 1 hull + gauss shield:")
    dc2 = DiceRoller(5, 2)
    rr = dc2.roundstoachieve(2)

    print("          Dreadnaught w/ 6 hull:")
    dc = DiceRoller(4, 7)
    rr = dc.roundstoachieve(2)
    print("          Dreadnaught w/ 4 hull + gauss shield:")
    dc2 = DiceRoller(5, 5)
    rr = dc2.roundstoachieve(2)
    print("          Dreadnaught w/ 2 hull + 2 gauss shield (ok):")
    dc = DiceRoller(6, 3)
    rr = dc.roundstoachieve(2)

    print("*** Dreadnaught w/ 2 plasma cannon + positron computer attacking!")
    print("          Interceptor w/ 1 hull:")
    dc = DiceRoller(4, 2)
    rr = dc.roundstoachieve(2, 2)
    print("           Interceptor w/ gauss shield")
    dc2 = DiceRoller(5, 1)
    rr = dc2.roundstoachieve(2, 2)

    print("          Cruiser w/ 2 hull:")
    dc = DiceRoller(4, 3)
    rr = dc.roundstoachieve(2, 2)
    print("          Cruiser w/ 1 hull + gauss shield:")
    dc2 = DiceRoller(5, 2)
    rr = dc2.roundstoachieve(2, 2)

    print("          Dreadnaught w/ 6 hull:")
    dc = DiceRoller(4, 7)
    rr = dc.roundstoachieve(2, 2)
    print("          Dreadnaught w/ 4 hull + gauss shield:")
    dc2 = DiceRoller(5, 5)
    rr = dc2.roundstoachieve(2, 2)
    print("          Dreadnaught w/ 2 hull + 2 gauss shield:")
    dc = DiceRoller(6, 3)
    rr = dc.roundstoachieve(2, 2)
