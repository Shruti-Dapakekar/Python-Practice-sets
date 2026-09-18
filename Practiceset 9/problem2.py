import random
# The game() function in a program lets a user play a game and returns the score as an integer.
# You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
def game():
    print("You are playing a game...")
    score = random.randint(1,62)
# fetch the hiscore.txt file
    with open("Practiceset 9/hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your Score :{score}")
    if (score>hiscore):
    #write this score to the file
        with open("Practiceset 9/hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()