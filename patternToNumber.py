import pdb

def symbolToNumber(symbol):
    if symbol == "A":
        number = 0
    elif symbol == "C":
        number = 1
    elif symbol == "G":
        number = 2
    elif symbol == "T":
        number = 3
    return number

def patternToNumber(Pattern):
    #pdb.set_trace()
    patternList = list(Pattern)
    if not patternList:
        return 0
    symbol = patternList[-1]
    prefix = patternList[:-1]
    #print symbol, prefix
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)

def readData(filename):
    with open(filename, 'r') as f:
        #f.readline() # Skip input line
        Pattern = f.readline()
        return Pattern.strip()

if __name__ == "__main__":
    Pattern = readData('dataset_3010_2.txt')
    result = patternToNumber(Pattern)
    print result