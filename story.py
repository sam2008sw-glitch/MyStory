import random

print("Welcome to the Adventure Game!")

hero_name = input("What is the hero's name? ")
hero_age = int(input("How old is the hero? "))
gold_amount = int(input("How much gold does the hero have? "))
strong_amount = int(input("How strong is the hero? (1-10): "))

hero_health = 10
items = ["sword", "potion", "shield"]


def show_status():
    print("Hero:", hero_name)
    print("Health:", hero_health)
    print("Gold:", gold_amount)


print("The adventure begins!")
print(hero_name, "is", hero_age, "years old and walks into a dark forest.")

print("The hero has these items:")
for item in items:
    print(item)

gold_found = random.randint(10, 50)
gold_amount += gold_found
print("The hero finds", gold_found, "gold!")

choice = input("Does the hero go left or right? ")

if choice == "left":
    print("The hero finds a dark cave.")
else:
    print("The hero walks towards an old castle.")

print("The hero finds a mysterious door.")
door_choice = input("Open the door? (yes/no) ")

if door_choice == "yes":
    print("The hero finds a treasure!")
    gold_amount += 100
else:
    print("The hero leaves the door alone.")

print("The hero arrives at an old bridge.")
print("A troll is blocking the way!")

fight_choice = input("Fight or run? ")

troll_health = 10

if fight_choice == "fight":
    print("The hero starts fighting the troll!")

    while troll_health > 0 and hero_health > 0:
        damage = random.randint(1, strong_amount)
        troll_health -= damage
        print("The hero deals", damage, "damage.")

        if troll_health > 0:
            troll_damage = random.randint(1, 3)
            hero_health -= troll_damage
            print("The troll attacks and the hero loses",
                  troll_damage, "health.")

    if hero_health > 0:
        print("The hero wins!")
        gold_amount += 50
        print("The hero gets 50 gold.")
    else:
        print("The hero loses the fight.")

else:
    print("The hero runs away.")

print("Final status:")
show_status()

print("The adventure ends!")
