import os 
import random
import json
from packages import playagain

    
def intro_message():
    width = os.get_terminal_size().columns
    print("Welcome to this fun Quiz of Marvel Avengers".center(width))
    print("There are a total of 20 questions, you can skip a question anytime".center(width))
    input("Press to start the fun ;) ".center(width))
    return True

intro = intro_message()


def game():
	print("\n==========Welcome to The Quiz ==========")
	score = 0
	with open("packages/question.json", ) as quiz:
		quiz = json.load(quiz)
		for i in range(20):
			no_of_questions = len(quiz)
			randomquestion = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {quiz[randomquestion]["question"]}\n')
			for option in quiz[randomquestion]["options"]:
				print(option)
				print()
			skip = input("Do you want to skip the Question and Move foward (yes/no):")
			if skip=="yes":
    				continue
			answer = input("\nEnter your answer: ")
			if quiz[randomquestion]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				print("\n==========Next Question==========")
				print()
				score+=1
			else:
				print("\nYou are incorrect")
				print("\n==========Next Question==========")
				
			del quiz[randomquestion]
		print(f"Your final score is {score}!\n\n")

if playagain.score == 0:
        playagain.playagain("lost")

if __name__ == "__main__":
	option = 1
	while option != 3:
		print('\n===========Marvel Quiz================')
		print('-----------------------------------------')
		print('1. Lets Begin')
		print('2. EXIT')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			game()
		elif choice == 2:
			exit()
			