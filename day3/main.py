f = open("input.txt", "r")
result = 0
rows = f.read().strip().split("\n")

collectedInfo = [];

def isSymbol(char):
    return char != "." and not char.isdigit()


for i, row in enumerate(rows):
    
    for idx, char in enumerate(list(row)):
        if isSymbol(char):
            # Above
            if i - 1 >= 0 and rows[i -1][idx].isdigit():
                collectedInfo.append({"row": i-1, "idx": idx})
            # Above left      
            if i - 1 >= 0 and idx - 1 >= 0 and rows[i-1][idx - 1].isdigit() and not rows[i -1][idx].isdigit():
                collectedInfo.append({"row": i-1, "idx": idx - 1})          
            # Above right
            if i - 1 >= 0 and idx + 1 <= len(rows[i-1]) - 1 and rows[i-1][idx + 1].isdigit() and not rows[i -1][idx].isdigit():
                collectedInfo.append({"row": i-1, "idx": idx + 1})
            # Down
            if i + 1 <= len(rows) -1 and rows[i +1][idx].isdigit():
                collectedInfo.append({"row": i+1, "idx": idx})   
            # Down left
            if i + 1 <= len(rows) -1 and idx - 1 >= 0 and rows[i+1][idx - 1].isdigit() and not rows[i +1][idx].isdigit():
                collectedInfo.append({"row": i+1, "idx": idx-1})
            # Down right
            if i + 1 <= len(rows) -1 and idx + 1 <= len(rows[i + 1]) - 1 and rows[i + 1][idx + 1].isdigit() and not rows[i +1][idx].isdigit():
                collectedInfo.append({"row": i+1, "idx": idx+1})
            # Left
            if idx - 1 >= 0 and row[idx - 1].isdigit():
                collectedInfo.append({"row": i, "idx": idx -1})
            # Right
            if idx + 1 <= len(rows) -1 and row[idx + 1].isdigit():
                collectedInfo.append({"row": i, "idx": idx+1})

for obj in collectedInfo:
    cRow = obj['row']
    cIdx = obj['idx']
    digitCollect = ""
    
    if rows[cRow][cIdx + 1].isdigit() and rows[cRow][cIdx - 1].isdigit():
        rightSide = ""
        leftSide = ""
        for i in range(cIdx, len(rows[cRow])):
           
            if rows[cRow][i] == "." or isSymbol(rows[cRow][i]):
                break
            
            rightSide += rows[cRow][i]
        
        for i in range(0, cIdx):
            if rows[cRow][i] == "." or isSymbol(rows[cRow][i]):
                leftSide = ""
            else:
                leftSide += rows[cRow][i]
                
        digitCollect += leftSide + rightSide;
    
    elif rows[cRow][cIdx + 1].isdigit():
        for i in range(cIdx, len(rows[cRow])):
           
            if rows[cRow][i] == "." or isSymbol(rows[cRow][i]):
                break
            
            digitCollect += rows[cRow][i]
    
    elif rows[cRow][cIdx - 1].isdigit():
        for i in range(0, cIdx + 1):
            if rows[cRow][i] == "." or isSymbol(rows[cRow][i]):
                digitCollect = ""
            else:
                digitCollect += rows[cRow][i]
    else:
        digitCollect += rows[cRow][cIdx]
    
    if len(digitCollect) > 0:
        result += int(digitCollect)
    
print(result)
   
    
    