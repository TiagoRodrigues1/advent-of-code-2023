f = open("input.txt", "r")
result = 0

for line in f.read().strip().split("\n"):
    cardPairNoGame = line.strip().split(":")
    
    cardPairs = cardPairNoGame[1].strip().split("|")
    
    left = list(filter(None, cardPairs[0].strip().split(" ")))
    right = list(filter(None, cardPairs[-1].strip().split(" ")))
    
    count = 0
    isFirst = True
    cardResult = 0
    
    for number in left: 
        if number in right:
            if isFirst:
                cardResult = 1
                isFirst = False    
            else:
                cardResult *=2
                
    result += cardResult 

print(result)