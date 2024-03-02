class Alien:
    def __init__(self):
        self.__name = ''
        self.__home = ''
        self.__health = 100
        self.__damage = 0

    def attack(self, aliens):
        aliens.receive_damage(self.__damage)

    def receive_damage(self, dmg):
        print(self.__name ,"received damage")
        self.__health -= dmg

    def is_dead(self):
        return self.__health <= 0

    def get_name(self):
        return self.__name

    def get_home(self):
        return self.__home

    def get_health(self):
        return self.__health

    def get_damage(self):
        return self.__damage

    def set_name(self,name):
        self.__name = name

    def set_home(self,home):
        self.__home = home

    def set_health(self,health):
        self.__health = health

    def set_damage(self,damage):
        self.__damage = damage


Alien1 = Alien()
Alien1.set_name('Alien 1')
Alien1.set_home('Agpton')
Alien1.set_health(100)
Alien1.set_damage(20)

Alien2 = Alien()
Alien2.set_name('Alien 2')
Alien2.set_home('Vanguard')
Alien2.set_health(100)
Alien2.set_damage(20)


Alien1.attack(Alien2)
print('Alien 2 current health', Alien2.get_health())

if Alien2.is_dead():
    print('Alien 2 is dead')
else:
    print('Alien 2 is alive')

Alien2.attack(Alien1)
print('Alien 1 current health:', Alien1.get_health())

if Alien1.is_dead():
    print('Alien 1 is dead')
else:
    print('Alien 1 is alive')

if Alien1.is_dead() and Alien2.is_dead():
    print('Alien 1 and Alien 2 are dead')