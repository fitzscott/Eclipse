import Ship
import random

class Fight:
    def __init__(self, attgrp, defgrp):
        self._attackers = attgrp
        self._defenders = defgrp
        random.seed()

    @property
    def attackers(self):
        return(self._attackers)

    @attackers.setter
    def attackers(self, val):
        self._attackers = val

    @property
    def defenders(self):
        return(self._defenders)

    @defenders.setter
    def defenders(self, val):
        self._defenders = val

    def rolldie(self):
        return(random.randint(1, 6))

    def findhighestinitiative(self):
        maxinit = 0
        for ship in self._attackers:
            if ship.initiative > maxinit:
                maxinit = ship.initiative
        for ship in self._defenders:
            if ship.initiative > maxinit:
                maxinit = ship.initiative
        return(maxinit)

    def attack(self, init, shooters, screamers):
        """
        The shooters list of ships will have zero or more ships
        with the appropriate initiative.
        """
        realshooters = []
        for ship in shooters:
            if ship.initiative == init and ship.damagepoints > 0:
                realshooters.append(ship)
                print(ship.name)
         
    def fighttothedeath(self):
        firstinit = self.findhighestinitiative()
        print("Highest initiative is " + str(firstinit))
        for init in range(firstinit):
            descinit = firstinit - init
            print("    Initiative: " + str(descinit))
            # defenders shoot first - odd, right?
            self.attack(descinit, self.defenders, self.attackers)
            self.attack(descinit, self.attackers, self.defenders)

if __name__ == "__main__":
    i1 = Ship.Ship("Interceptor 1", 1, 3)
    i2 = Ship.Ship("Interceptor 2", 1, 3)
    i3 = Ship.Ship("Interceptor 3", 1, 3)
    c1 = Ship.Ship("Cruiser 1", 2, 2)
    d1 = Ship.Ship("Dreadnought 1", 3, 1)
    agrp = [d1, i2]
    dgrp = [c1, i1, i3]
    f = Fight(agrp, dgrp)
    f.fighttothedeath()

