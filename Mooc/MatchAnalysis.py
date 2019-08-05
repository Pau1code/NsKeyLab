import random

def printIntro():
    print("This programmer is to simulate certain competition including two players: A and B")
    print("Programmer running needs the ability values of the two players(Expressed in decimal numbers between 0 and 1)")


def getInputs():
    a = eval(input("Please input the ability value of A player:"))
    b = eval(input("Please input the ability value of B player:"))
    n = eval(input("Match number:"))
    return a, b, n


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Competition starting, simulation {} matches".format(n))
    print("Player A wins {} matches, proportion is {:0.1%}".format(winsA, winsA/n))
    print("Player B wins {} matches, proportion is {:0.1%}".format(winsB, winsB/n))


def simOneGame(probA, proB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random.random() < proB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b == 15


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n,probA, probB)
    printSummary(winsA, winsB)

if __name__ == '__main__':
    main()





















