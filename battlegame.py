# Player Choices
wizard = ("Wizard")
elf = ("Elf")
human = ("Human")
orc = ("Orc")

# Player Statistics
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 25

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 250

# Dragon Statistics
dragon_hp = 300
dragon_damage = 50

# Character Selection Function
while True:
    print("Enter 1 or type Wizard for Wizard")
    print("Enter 2 or type Elf for Elf")
    print("Enter 3 or type Human for Human")
    print("Enter 4 or type Orc for Orc")

    character = input("Choose your character: ").lower()
    if character == "1" or character.lower() == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4" or character == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif character == "5" or character == "exit":
        print("Goodbye!")
    else:
        print("Invalid choice. Please choice another option")

# Tell User About Their Choice
print ("You have chosen the character: " , character)
print ("Your health points are: " , my_hp)
print ("Your damage is: " , my_damage)

# Battle Function
while True:
    dragon_hp = dragon_hp - my_damage
    print ("The " + str (character) + " damaged the Dragon!")
    if dragon_hp <= 0:
        print ("The dragon has lost the battle.")
        break
    my_hp = my_hp - dragon_damage
    print ("You have been hit by the dragon for " + str (dragon_damage) + "! Your current hits points are " + str (my_hp))
    if my_hp <= 0:
        print ("You have lost the battle.")
        break
