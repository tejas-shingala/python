import random

def game():
    random_num = random.randint(1,100)
    while True:
        user_num = input("enter number(1-100): ")
        if user_num.isdigit():
            user_num = int(user_num)
            if 1 <= user_num <= 100:
                break
            else:
                print("must be a number between 1-100")
        else:
            print("Must be a number!")

    guess=1

    while True:
        if random_num > user_num:
            user_num = int(input("higher number please: "))
        elif random_num < user_num:
            user_num = int(input("lower number please: "))
        else :
            break
        guess += 1

    print(f"you won the game in {guess} guesses!")
    replay = input("do you want to play again(yes/no)? ")
    if "yes" in replay:
        game()
    else:
        print("thank you for playing!")

game()


