
#imports
#global variables
#classes



from tkinter import N


class Character:
    
    
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f'Name:{self.name}\nHealth:{self.health}\nDamage : {self.damage}\n Armor : {self.armor}\n'
#functions

def hello():
    print("Hello world")
#main code





