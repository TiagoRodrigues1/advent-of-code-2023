f = open("input.txt", "r")
lines = f.read().strip().split("\n")

for idx, line in enumerate(lines):
    cardPairNoGame = line.strip().split(":")
    cardNumber = cardPairNoGame[0].strip().split(" ")[-1]
    cardPairs = cardPairNoGame[1].strip().split("|")
    
    left = list(filter(None, cardPairs[0].strip().split(" ")))
    right = list(filter(None, cardPairs[-1].strip().split(" ")))
    
    count = 0
    isFirst = True
    cardResult = 0
    
    for number in left: 
        if number in right:
            count +=1
            lines.append(lines[int(cardNumber) - 1 + count])

        

print(len(lines)) 
