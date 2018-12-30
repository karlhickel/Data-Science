#Karl Hickel

import math

NUM_ATTRIBUTES = 2
TRAIN_DATA_FILE = "reg_train.csv"


#read the train file and return the data as two lists (ind and dep variables)
def readData(fname):
    data = []
    x = []
    y = []
    f = open(fname,"r")
    for i in f:
        instance = i.split(",")
        x.append(float(instance[0].strip()))
        y.append(float(instance[1].strip()))

    f.close()
    data.append(x)
    data.append(y)
    return data

def printParams(params):
    print("The value of B0 (intercept) is: ", params[0])
    print("The value of B1 (slope) is: ", params[1])

#The linear regression algorithm. Takes a list of lists as input
def lreg(ind_variable,dep_variable):
    params = []
    B0 = 0.0
    B1 = 0.0
    #This is where I calculate the respsective means
    xMean = sum(ind_variable)/len(ind_variable)
    yMean = sum(dep_variable)/len(dep_variable)
    #Variables to store for B1
    num = 0
    den = 0
    
    
    #Find the lengdth of the whole data set and calculate num and den. 
    for k in range(len(dep_variable)):
        num += ind_variable[k] * (dep_variable[k] - yMean)
        den += ind_variable[k] * (ind_variable[k] - xMean)
        
    B1 = num/den
    B0 = yMean - B1*xMean
    #This is where I added the results to each  respective B0 and B1 values. 
    #PS this is where i needed assistance. 
    params.append(B0)
    params.append(B1)
    return params


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
    train_matrix = readData(TRAIN_DATA_FILE)
    parameters = lreg(train_matrix[0],train_matrix[1])
    printParams(parameters)
