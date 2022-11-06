
import random
from statistics import mean, median, mode


list_of_attempts=[] 
name=input("Please enter your name: ")
print(f"Hello {name}! Welcome to the Number Guessing Game")

def start_game():

        answer=random.randint(1,100) 
        attempt=0 
        while True:
            attempt=attempt+1
            guess=input("Pick a number between 1 and 100: ")
            try:
                guess=int(guess)
                if guess>100 or guess<1:
                    raise ValueError()
            except ValueError:
                    print("Not a valid value. Please pick a number between 1 and 100")
                    continue
 
            if guess==answer:
                list_of_attempts.append(attempt)
                high_score=min(list_of_attempts)
                print("Got it")
                print(f"You guessed the number in {attempt} attempts.") 
                if attempt<=10:
                    print(f"Great score, {name}!")
                elif attempt>10:
                    print(f"You can do it better {name}! Keep trying")
                while True:
                    play_again=input("Do you want to play again? Answer: Y/N ")
                    if play_again.lower()=="y" and high_score>1:
                        print(f"Your highest score is {high_score}. You can beat it!")
                        start_game() 
                    elif play_again.lower()=="y" and high_score==1:
                        print(f"You reached the highest score: {high_score}! Congratulations!")
                        start_game() 
                    elif play_again.lower()=="n":
                        print(f"Thank you for playing {name}!") 
                        print(f"Number of attempts: {len(list_of_attempts)}")
                        print(f"Scores: {list_of_attempts}")
                        mode_score=mode(list_of_attempts)
                        print(f"The mode is: {mode_score}")
                        median_score=median(list_of_attempts)
                        print(f"The median is: {median_score}")
                        mean_score=mean(list_of_attempts)
                        print(f"The mean is: {round(mean_score,2)}")
                        print(f"Your high score is: {high_score}")  
                    elif  play_again.lower()!="y" or play_again.lower()!="n":
                        print("Please answer Y or N")
                        continue
                    break
                break
            elif guess > answer:
                print("It's lower")
                continue 
            elif guess<answer:
                print("It's higher")
                continue
        
start_game()