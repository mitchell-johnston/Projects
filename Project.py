import random
def play(): 
    print("hello world, wanna play a game")
    user_choice=input('rock, paper or scissors?').lower()
    print("you chose "+ user_choice)
    choices=['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print("computer chose "+computer_choice)
    if user_choice =="rock" and computer_choice =="rock":
        print("tie")
    elif user_choice =="paper" and computer_choice =="paper":
        print("tie")
    elif user_choice =="scissors" and computer_choice=="scissors":
        print("tie")
    elif  user_choice =="rock" and computer_choice =="paper":
        print("computer wins")
    elif user_choice =="paper" and computer_choice =="scissors":
        print("computer wins")
    elif user_choice =="paper" and computer_choice =="rock":
        print("user wins")
    elif user_choice =="scissors" and computer_choice =="paper":
        print("user wins")
    elif user_choice =="scissors" and computer_choice =="rock":
        print("computer wins")
    elif user_choice =="rock" and computer_choice=="scissors":
        print("user wins")
    else:
        print("thats not a choice, dummy")
def main():
    play()
    while True:
        choice2= input("Wanna play again? yes or no ").lower()
        if choice2== "yes":
            play()
        else:
                break
main()