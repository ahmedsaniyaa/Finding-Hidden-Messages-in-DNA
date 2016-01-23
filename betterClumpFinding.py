from computingFrequencies import computingFreqs
from numberToPattern import numberToPattern
from patternToNumber import patternToNumber

def betterClumpFinding(Genome, k, t, L):
    genomeList = list(Genome)
    frequentPatterns = []
    clump = []
    for i in range(4**k - 1 + 1):
        clump.insert(i, 0)
    text = Genome[0:L]
    frequencyArray = computingFreqs(text,k)
    for i in range(4**k-1+1):
        if frequencyArray[i] >= t:
                clump[i] = 1
    for i in range(len(genomeList) - L + 1):
        firstPattern = Genome[i-1:i-1+k]
        index = patternToNumber(firstPattern)
        frequencyArray[index] = frequencyArray[index]-1
        lastPattern = Genome[i+L-k:i+L-k+k]
        index = patternToNumber(lastPattern)
        frequencyArray[index] = frequencyArray[index]+1
        if frequencyArray[index] >= t:
                clump[index] = 1
    for i in range(4**k):
        if clump[i] == 1:
            pattern = numberToPattern(i,k)
            frequentPatterns.append(pattern)
    return frequentPatterns

if __name__ == "__main__":
    Genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    k = 5
    L = 50
    t = 4
    result = betterClumpFinding(Genome, k, t, L)
    print result