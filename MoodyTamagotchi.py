#A needy tamagotchi which changes its mood constantly
import random

check_tamagotchi = input("Would you like to check on your tamagotchi? Please type \"Y\" for yes or \"N\" for no:")

while check_tamagotchi == "Y":
    tamagotchi_mood = random.choice([1,2,3,4,5])
    if tamagotchi_mood == 0 or 1:
         print("Your tamagotchi is happy.")
    elif tamagotchi_mood == 2:
         print("Your tamagotchi is sad.")
    elif tamagotchi_mood == 3:
        print("Your tamagotchi is sleeping.")
    elif tamagotchi_mood == 4 or 5:
        print("You tamagotchi is hungry.")
    check_tamagotchi = input("Would you like to check on your tamagotchi again?")

print("Bye bye!")

#for some reason the tamagotchi is always happy...?