from time import sleep
seconds = 2.5
seconds_less = 1.4
print("welcome to england")
sleep(seconds)
city = str(input("what city do you want to teleport to?: "))
sleep(seconds)
print("you are now teleporting to " + city)
sleep(seconds)
print("you can see big ben in front of you")
sleep(seconds)
print("there are 3 NPC'S infront of you")
sleep(seconds_less)
class_choice = int(input("Press 1 to speak to death, press 2 to speak to life, press 3 to speak to balance: "))
sleep(seconds_less)
if class_choice == 1:
    class_confirmation = str(input("Hello i am death, are you sure you want to be a necromancer: "))
    
    
if class_confirmation == "yes":
    print("You are now a necromancer")
else:
    class_confirmation == "no"
    print("noob")

