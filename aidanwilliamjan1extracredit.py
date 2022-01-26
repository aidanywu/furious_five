import random


minimum = int(input("min: "))
maximum = int(input("max: "))
rando = random.randint(minimum, maximum)
print(rando)


def guess(min, max):
    number = input("Your Guess: ")
    try:
        if int(number) == rando:
            print("youre correct")
            return
        elif int(number) != rando:
            yesorno = input("Wrong D: do you want ot play again?")
            if yesorno == "yes":
                return guess(min, max)
            else:
                print("ok")
                return
    except ValueError:
        print("enter an integer fucking dumbass")
        return guess(min, max)


guess(minimum, maximum)
