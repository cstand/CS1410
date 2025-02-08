class Pokemon:
    def __init__(self, name, type_name, number, max_hp, hp):
        self._name = name
        self._typeName = type_name
        self._number = number
        self._maxHp = max_hp
        self._hp = hp
        return

    def getName(self):
        return self._name

    def getMaxHP(self):
        return self._maxHp

    def getHP(self):
        return self._hp

    def setName(self, new_name):
        self.mName = new_name
        return

    def takeDamage(self, damage):
        self._hp = self._hp - self.damage
        if self._hp < 0:
            self._hp = 0
        return

    def takePotion(self, heal):
        self._hp -= heal
        if self._hp > self._maxHp:
            self._hp = self._maxHp
        return

    def __str__(self):
        s = f"{self._name.upper()}{{{self._typeName}:{self._number}}} "
        s += f"Max HP: {self._maxHp} "
        s += f"Current HP: {self._hp}"
        return s
