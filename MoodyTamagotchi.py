import random

tamagotchi_mood = 0

while True:
    check_tamagotchi = input("Would you like to check on your tamagotchi? Please type \"Y\" for yes or \"N\" for no:")

    if check_tamagotchi == "Y":
        tamagotchi_mood = random.randint(0, 5)
        if tamagotchi_mood == 0 or tamagotchi_mood == 1:
            print("Your tamagotchi is happy.")
        elif tamagotchi_mood == 2:
            print("Your tamagotchi is sad.")
            pet_tamagotchi = input("Would you like to pet your tamagotchi? Please type \"Y\" for yes or \"N\" for no:")
            if pet_tamagotchi == "Y":
                print("You pet your tamagotchi. It's feeling better now.")
            else:
                print("You chose not to pet your tamagotchi.")
        elif tamagotchi_mood == 3:
            print("Your tamagotchi is sleeping.")
        elif tamagotchi_mood == 4 or tamagotchi_mood == 5:
            print("Your tamagotchi is hungry.")
            feed_tamagotchi = input("Would you like to feed your Tamagotchi? Please type \"Y\" for yes or \"N\" for no:")
            if feed_tamagotchi == "Y":
                print("You fed your tamagotchi. It's no longer hungry!")
            else:
                print("You chose not to feed your tamagotchi.")
    else:
        break

print("Bye bye!")
