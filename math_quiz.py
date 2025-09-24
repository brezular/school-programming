"""
TASK:
The program gives arithmetic problems.

INPUT REQUIREMENTS:
The number of digits in the problems increases with each level:

Level 1 = numbers from 1 to 9

Level 2 = numbers from 10 to 99

Level 3 = numbers from 100 to 999

etc.

The user is timed for each problem. If the time limit is exceeded, the answer is counted as incorrect.

The time limit doubles with each level (due to increasing difficulty).

The number of points for correct answers also increases by 1 each level.

The number of points for incorrect answers also increases by 1 each level.

OUTPUT REQUIREMENTS:
The program ends when the maximum number of bad points is reached or the user quits by typing 'q'.

The program displays the number of correct points achieved and the total number of questions answered.
"""

import time
import random

END_OF_GAME = False

OPERATION ="+-*/"
level = 1

# The number of seconds the user has to solve the problem in Level 1; this will increase in later levels.
TIME_LIMIT = 5    

bad_answer = 0
good_answer = 0
count_answer_level = 0
count_answer_game = 0

# max pocet question per level
MAX_QUESTION_LEVEL = 3    

# game is ended when this limit is reached
MAX_BAD_POINTS = 8


def compute_task(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:
        return int(a / b)

def generate_nums(level):
    while True:
        # Set the number range for each level accordingly
        a = random.randint((10**level)//10, (10**level)-1)   
        b = random.randint((10**level)//10, (10**level)-1)

        if a < b:
            a, b = b, a

        if b!=0 and a % b == 0:                  # Return a,b if b can be divided by b
            return a, b

def check_score(count_answer_level, level, TIME_LIMIT, END_OF_GAME, result_user, good_answer, bad_answer, count_answer_game):
    # If the maximum number of questions for the level is reached:
    if count_answer_level == MAX_QUESTION_LEVEL:
        level+=1                                
        count_answer_level = 0                # Reset number of task for level 
        TIME_LIMIT*=2                         # Double time limit for each level
        print(f"\n*** Level {level}, {TIME_LIMIT} seconds for a task ****")

    if result_user == 'q' or bad_answer >= MAX_BAD_POINTS:
        display_stats(good_answer, count_answer_game)
        END_OF_GAME = True

    return count_answer_level, level, TIME_LIMIT, END_OF_GAME

def play_game(bad_answer, good_answer, count_answer_level, count_answer_game):

    count_answer_game+=1

    print(f"\nTask {count_answer_game}: \t{num1} {operator} {num2} = ", end=" ")
    
    # Start timer for user
    start_time = time.time()                    

    while True:
        result_user = input()
        
        # If time is up, finish a loop
        if time.time() - start_time > TIME_LIMIT:         
            print("Time's up!")
            bad_answer+=level
            break
        
        if not result_user.isdigit():               # Finish a loop if user's choice is not a digit
            print(f"Wrong! '{result_user}' is not a digit")
            bad_answer+=level
            break
        else:
            result_user = int(result_user)  # Convert user's choice to int    
   
        if result_pc == result_user:  
            print("Good!")
            good_answer+=level
            break
        else:
            print(f"Wrong! Right answer is {result_pc}")
            bad_answer+=level
            break
      
    count_answer_level+=1

    return bad_answer, good_answer, count_answer_level, result_user, count_answer_game

def display_stats(good_answer, count_answer_game):
    print(f"\n*** GAME OVER! You've got {good_answer} points from {count_answer_game} tasks ***")
    

# +------- Main Program -------------+   

print("Welcome to the arithmetic practice game.\n")
print("You get one good point for each correct answer.")
print("You get one bad point for each wrong answer.\n")
print(f"The game ends if you get more than {MAX_BAD_POINTS} bad points.")
print(f"Each level contains {MAX_QUESTION_LEVEL} questions.")

key = None
while key != "c":
    key = input("\nPress 'c' to start the game: ") 
    
print(f"\n*** Level {level}, {TIME_LIMIT} seconds for task ****")

    
while True:
    # Generate an arithmetic operation
    operator = random.choice(OPERATION)     

    # Generate numbers 1 and 2 
    num1, num2 = generate_nums(level)        
  
    # Calculate the arithmetic operation between num1 and num2
    result_pc = compute_task(num1, num2, operator)  

    bad_answer, good_answer, count_answer_level, result_user, count_answer_game = play_game(bad_answer, good_answer, count_answer_level, count_answer_game)

    count_answer_level, level, TIME_LIMIT, END_OF_GAME = check_score(count_answer_level, level, TIME_LIMIT, END_OF_GAME, result_user, good_answer, bad_answer, count_answer_game)

    if END_OF_GAME:
        break


     
        

    


    



    

    

