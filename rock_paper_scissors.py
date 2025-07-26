""" Rock, Paper, Scissors against the computer
    2025 brezular
"""
import random

# Intial points for player and computer
point_player = point_computer = 0


# Display stats
def stats(a, h, p):
     print(f"{a}! Player point(s): {h}, Computer point(s): {p}")

# Introduction
print(f"\nTime to play Rock, Paper, Scissors against the computer!")
print(f"Enter 's' for scissors, 'p' for paper, or 'r' for rock.\n")


# Read number of rounds
max_round = input("Enter number of rounds: ")
while not max_round.isdigit():
     print(f"\n'{max_round}' is not digit")
     max_round = input("Enter number of rounds: ")
max_round = int(max_round)


# Main loop of game   
for round in range(1, max_round+1):

     # Player choice - read input until player enter r, p, s
     volba_hrac = input(f"\n{round}. Enter your choice: ")
     while not volba_hrac in 'rps':
          print(f"'{volba_hrac}' is not a valid choice")
          volba_hrac = input(f"\n{round}. Enter your choice: ")

     
     # Computer choice
     volba_pc = random.choice(['rock', 'paper', 'scissors'])
     print(f"Computer entered: {volba_pc}")

     # Determine Round Result - Player Wins
     if (volba_hrac == 'r' and volba_pc =='scissors') or \
        (volba_hrac == 'p' and volba_pc =='rock') or \
        (volba_hrac == 's' and volba_pc =='paper'):
          point_player+=1              
          stats("You won this round", point_player, point_computer)

     # Draw     
     elif (volba_hrac == 'r' and volba_pc =='rock') or \
          (volba_hrac == 'p' and volba_pc =='paper') or \
          (volba_hrac == 's' and volba_pc =='scissors'):
          stats("You draw in this round", point_player, point_computer)          

     # Computer victory
     else:
          point_computer+=1              
          stats("You lost this round", point_player, point_computer)

# Final evaluation
if point_player > point_computer:
     print(f"\nGAME OVER!!! You win. Congratulations! \U0001f600")
elif point_player < point_computer:
     print(f"\nGAME OVER!!! You lose. Better luck next time! \U0001F923")
else:
     print(f"\nGAME OVER!!! Draw. Not bad! \U0001F606")

        


    
