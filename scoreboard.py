def init(_maxcount=20):
    #Initiate scoreboard
    global scoreboard
    global maxcount
    scoreboard = []
    maxcount = _maxcount

def addScore(name, score, descend = True):
    #Add score to scoreboard
    global scoreboard
    scoreboard.append((name,score))
    scoreboard = sorted(scoreboard, key=lambda scoreboard: scoreboard[1], reverse = descend)
    if(len(scoreboard)>maxcount):
       #if scoreboard has more scores than its max delete the smallest score
       del scoreboard[len(scoreboard)-1]

def clearScore():
    #clear scoreboard
    global scoreboard
    scoreboard = []


def setMaxCount(_maxcount):
    #Set max score count
    global maxcount
    maxcount = _maxcount

def getName(index):
    #get name of certain index
    global scoreboard
    return scoreboard[index][0];

def getScore(index):
    #get score of certain index
    global scoreboard
    return scoreboard[index][1];

def main():
    #for testing
    init()
    print ("Press Ctrl+C to exit \n")
    while(True):
        name = raw_input("Please write your name: ")
        score = int(raw_input("Please write your score: "))
        addScore(name, score)
        print("name / score\n")
        for i in range(len(scoreboard)):
            print "%s / %d" %(getName(i), getScore(i))
main()
