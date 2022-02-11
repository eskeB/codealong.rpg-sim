from resources import Character

def main(): #hp, damage, armor
    Linus = Character("Lelle", 15, 6, 5)
    Adam = Character("Adam", 3, 1, 1)
    Pelle = Character("Pelle", 5, 20, 1)
    Erik = Character("Erik", 15, 6, 5)
    
    
    print(Linus)
    print(Adam)
    print(Pelle)
    print(Erik)

if __name__ == "__main__":
    main()