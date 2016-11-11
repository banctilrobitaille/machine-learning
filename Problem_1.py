import csv
import numpy as np


def gini(prob):
    return prob*prob

def indexGini(prob):
    sum_ = 0
    for p in prob:
        sum_ += gini(prob)

    return 1-sum_

def getData(feat1, feat2, feat3):
 i = 0
 with open('02_homework_dataset.csv', newline='') as csvfile:
     file = csv.reader(csvfile, delimiter=',', quotechar='|')
     next(file)
     for row in file:
        feat1[0,i] = row[0]
        feat1[1,i] = row[3]
        feat2[0, i] = row[1]
        feat2[1, i] = row[3]
        feat3[0, i] = row[2]
        feat3[1, i] = row[3]
        i = i+1



