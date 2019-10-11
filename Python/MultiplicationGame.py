import random

print("Welcome to the Multiplication Game!")
print("What is your name?")
name = input()
print("Good luck "+name+"!")
gameOver = False
level = 0
correct = 0
lvlcount = 0
factor1 = random.randint(1,12)
factor2 = random.randint(0, level)
while not gameOver:
    factor1 = random.randint(1,12)
    factor2 = random.randint(0, level)
    answer = factor1 * factor2
    print("What is "+str(factor1)+" * "+str(factor2)+"?")
    answer2 = int(input())
    if answer == answer2:
        correct+=1
        lvlcount+=1
        print("Correct")
        if lvlcount >= 10:
            level+=1
            lvlcount = 0
            print("Level up! Now you are at level "+str(level))
    else:
        gameOver = True
        print("Game over!")
print("Good Job "+name+"!")
print("You got "+str(correct)+" questions correct, to level "+str(level))
