class Ship:

    def __init__(self, nm, dmg, init, hitbonus=0, shieldbonus=0):
        self._name = nm
        self._damagepoints = dmg
        self._initiative = init
        self._hitbonus = hitbonus
        self._shieldbonus = shieldbonus
        self._weapons = []

    @property
    def name(self):
        return(self._name)

    @property
    def damagepoints(self):
        return(self._damagepoints)

    @damagepoints.setter
    def damagepoints(self, val):
        self._damagepoints = val

    @property
    def initiative(self):
        return(self._initiative)

    @initiative.setter
    def initiative(self, val):
        self._initiative = val

    @property
    def hitbonus(self):
        return(self._hitbonus)

    @hitbonus.setter
    def hitbonus(self, val):
        self._hitbonus = val

    @property
    def shieldbonus(self):
        return(self._shieldbonus)

    @shieldbonus.setter
    def shieldbonus(self, val):
        self._shieldbonus = val

    def addweapon(self, dmg):
        self._weapons.append(dmg)

    def willbehit(self, basetohit, hitroll):
        return(basetohit <= hitroll + self.shieldbonus)

    def willbedestroyed(self, basetohit, hitroll, dmg):
        if self.willbehit(basetohit, hitroll):
            return(self.damagepoints <= dmg)

    def applyhit(self, dmg):
        self.damagepoints -= dmg
        return (self.damagepoints <= 0)

if __name__ == "__main__":
    intcpt = Ship("Interceptor", 1, 3)
    intcpt.addweapon(1)
    if intcpt.willbehit(6, 6):
        print("6 hits on a 6 to hit.")    
    if intcpt.willbehit(basetohit=5, hitroll=6):
        print("6 hits on a 5 to hit.")
    if intcpt.willbedestroyed(5, 6, 1):
        print("Interceptor will be destroyed by 1 hit.")
    if intcpt.applyhit(1):
        print("Interceptor destroyed.")

