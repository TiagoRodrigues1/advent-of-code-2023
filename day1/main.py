f = open("input.txt", "r")
sum = 0;
firstDigit = ""
lastDigit = ""
word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def hasMoreDigits(currentPos, arr):
    for i in range(currentPos, len(arr)):
        if arr[i].isdigit():
            return True
        elif startsWith(i, arr) > 0:
            return True


def startsWith(idx, line):
    for i, word_digit in enumerate(word_digits):
        if line[idx:].startswith(word_digit):
           return i + 1;
    return 0

for line in f.read().strip().split("\n"):
    for idx, char in enumerate(line):
        st = startsWith(idx, line);

        if st > 0 and firstDigit == "":
            firstDigit = str(st);

        if char.isdigit() and firstDigit == "":
            firstDigit = char
        
        if firstDigit != "":
            st = startsWith(idx, line)

            if st > 0 and not hasMoreDigits(idx + 1, line):
                lastDigit = str(st);

            if char.isdigit() and not hasMoreDigits(idx + 1, line):
                lastDigit = char

    if not lastDigit:
        lastDigit = firstDigit


    print(firstDigit + lastDigit)
    sum += int(firstDigit + lastDigit)
    firstDigit = ""
    lastDigit = ""

print(sum)