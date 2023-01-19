import random

def password_generator():
    """ Generates password from the given list"""

    # list of password 
    animals = ["Goat","Tiger","Elephant","Giraffe","Dog","Cow","Cat","Panda","Kangaroo"]
    names = ["Messi","Ronaldo","Ozil","Neymar","Haaland","Kane","Maguire","Salah"]
    food = ["Grass","Chicken","Legpiece","Lyammalyamma","Buff","Pork","Steak"]

    
    # list = [i+j+k for i in animals for j in names for k in food]
    # print(len(set(list)))

    # Prompt user for number of passwords needed
    print("\nPassword Generator\n==================\n")

    #while loop to generate and print password 
    while True:
        try:
            # input the number of password you want to generate
            amount = int(input("How many passwords are needed?: "))
            
            # Check if input is a valid number within range
            if 0<amount<=24:
                # Generate requested number of passwords
                for x in range(amount):
                    a = random.choice(animals)+random.choice(names)+random.choice(food)
                    print(f"{x+1}--> {a}")
                break
            else:
                print("Please enter a value from 1 to 24")
                continue

        #if user enter a string 
        except :
            print("Please enter a number. ")


password_generator()
