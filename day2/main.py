f = open("input.txt", "r")

max  = {
    'green': 13,
    'red':12,
    'blue':14
    }   
possibleSum = 0
    

for currentGame in f.read().strip().split("\n"):
    gameId = currentGame[5:currentGame.index(':')]
    isFirst = True
    isImpossible = False
    
    for set in currentGame.split(';'):
        if(isFirst):
            set = set[set.index(':') + 1:len(set)]
            isFirst = False
        
        for entry in set.split(','):
            
            entrySep = entry.strip().split(' ')
            if int(entrySep[0]) > max[entrySep[1]]:
                isImpossible = True
                break

    if not isImpossible:
        possibleSum += int(gameId)  
print(possibleSum)       