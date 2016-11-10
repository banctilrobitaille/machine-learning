import csv
import numpy as np

with open('02_homework_dataset.csv', newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in file:
        print(row)



def gini(prob):
    return prob*prob

def indexGini(prob):
    sum_ = 0
    for p in prob:
        sum_ += gini(prob)

    return 1 - sum_

#def createLeftBranch(feat_data, threshold):
    #j = 0
    #left_branch = np.array(feat_data.shape)
    #for value in feat_data[0,:]:
        #if  value <= threshold:
           #left_branch[0,j] = value
           #left_branch[1,j] =