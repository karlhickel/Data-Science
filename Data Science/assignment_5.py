import math

#valueSplit is a list of 2 items. The first is number of positive examples,
#the second is the number of negative examples
def calcEntropy(valueSplit):
    h = 0.0
    plus = valueSplit[0]
    negative = valueSplit[1]
    total = plus + negative
    part1 = (-plus/total) * math.log2(plus/total)
    part2 = (negative/total) * math.log2(negative/total)
    h = part1 - part2
    print(h)
    
     
    return h








#rootValues is a list of the values at the parent node. It consists of 2 items.
#The first is number of positive examples,
#the second is the number of negative examples
#descendantValues is a list of lists.  Each inner list consists of the number of positive
#and negative examples for the attribute value you want to split on.
def calcInfoGain(rootValues,descendantValues):
    gain = 0.0
    EntropyrootSplit = calcEntropy(rootValues)
    Entropydescend1 = calcEntropy(descendantValues[0])
    Entropydescend2 = calcEntropy(descendantValues[1])
    gain = EntropyrootSplit - (Entropydescend1 * (sum(descendantValues[0])/(sum(descendantValues[0])+sum(descendantValues[1]))) + (Entropydescend2 * (sum(descendantValues[1])/(sum(descendantValues[0])+sum(descendantValues[1])))))
    
    
    return gain








if __name__ == "__main__":
    attributeName = "Humidity"
    rootSplit = [9,5] # 9 positive, 5 negative examples
    descendantSplit = [[3,4],[6,1]]
    
    ig = calcInfoGain(rootSplit, descendantSplit)
    print("The information gain of splitting on ",attributeName," is: ",ig," bits")