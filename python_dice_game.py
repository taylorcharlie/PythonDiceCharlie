#Roll dice game. 
#Two player
import random

#Initialise player scores at 0
player1_score = 0
player2_score = 0

#Repeats game 10 times before final score.
for i in range(10):
    
    #Generates numbers (1, 6) for each player.
    player1_value = random.randint(1, 6)
    player2_value = random.randint(1, 6)
    
    #Display's number the player gets.
    print("Player 1 rolled: ", player1_value)
    print("Player 2 rolled: ", player2_value)
    
    # Selection: based on comparison of the values, take the appropriate path through the code.
    if player1_value > player2_value:
        print("Player 1 wins.")
        player1_score = player1_score = 1 #this is how we increase a variable
    elif player2_value > player1_value:
        print("Player 2 wins")
        player2_score = player2_score + 1 
    else:
        print("Its a draw")
    
    input("Press enter to continue.") # wait for input yo proceed 

print("### Game Over ###")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)