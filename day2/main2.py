f = open("input.txt", "r")

allCubeMax = []
total = 0
for currentGame in f.read().strip().split("\n"):
    isFirst = True
    maxEachCube  = {
        'green': 0,
        'red':0,
        'blue':0
        }
    for set in currentGame.split(';'):
        if(isFirst):
            set = set[set.index(':') + 1:len(set)]
            isFirst = False
        
        for entry in set.split(','):
            entrySep = entry.strip().split(' ')
            if int(entrySep[0]) > maxEachCube[entrySep[1]]:
                maxEachCube[entrySep[1]] = int(entrySep[0])
                    
    allCubeMax.append(maxEachCube)
    total += maxEachCube['green'] * maxEachCube['red'] * maxEachCube['blue']     
       
print(total)