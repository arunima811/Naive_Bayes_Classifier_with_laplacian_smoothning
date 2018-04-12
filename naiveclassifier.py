# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 17:06:59 2018

@author: Aru
"""
"""randomise split"""

import csv 
from collections import Counter, defaultdict
import numpy as np
outcome = []

#calculating the conditional probabilities 
def occurrences(outcome):
    if type(outcome[0]) == type([]):
        outcome = outcome[0]
    no_of_examples = len(outcome)
    prob = Counter(outcome)
    for key in prob.keys():
        prob[key] = prob[key] / float(no_of_examples)
    return prob
    #print prob 
    

#Calculating conditional probabilities with laplacian smoothing with a factor lf
def occurrences_with_ls(outcome, tot_outcomes, lf):
    if type(outcome[0]) == type([]):
        outcome = outcome[0]
    no_of_examples = len(outcome)
    prob = Counter(outcome)
    for k in prob:
        prob[k]+=1
    for key in prob.keys():
        prob[key] = prob[key] +lf/ ((lf+float(no_of_examples))+tot_outcomes)
    return prob

#Spliting the dataset into training data and test data so that the classifier runs on a single .csv file
def splitDataset(fulldataset, splitRatio):
	trainSize = int(len(fulldataset) * splitRatio)
	return fulldataset[:trainSize], fulldataset[trainSize:]


"""getting the splitted training set with their respective outcomes for getting trained. The test cases are being sent as new_sample. """
def naive_bayes(training, outcome, new_sample, tot_outcomes, lf):
    classes     = np.unique(outcome)
    rows, cols  = np.shape(training)
    
    likelihoods = {}
    for cls in classes:
        likelihoods[cls] = defaultdict(list)
        
    class_probabilities = occurrences(outcome)
    
    for cls in classes:
        row_indices = np.where(outcome == cls)[0]
        
        subset = []
        for ri in row_indices:
            if ri<rows:
                subset.append(training[ri])
        
        r, c = np.shape(subset)
        
        for j in range(0, c-1):
            temp = []
            for k in range(r):
                temp.append(subset[k][j])
            likelihoods[cls][j].append(temp)
    
    for cls in classes:
        for j in range(len(likelihoods[cls])):
            likelihoods[cls][j] = occurrences_with_ls(likelihoods[cls][j],tot_outcomes, lf) 
    print ('likelihoods being printed as dictionary of dictionary with dict[classes][columns](probability of each variable)')
    print ('likelihoods are :{}').format(likelihoods)   
    
    """probabilities of the given test cases get calculated here"""
    results = {}
    for cls in classes:
         class_probability = class_probabilities[cls]
         for i in range(len(new_sample)):
             relative_values = likelihoods[cls][i]
             if type(new_sample[0]) == type([]):
                 new_sample = new_sample[0]
             for keys in range(len(relative_values)):
                 if new_sample[i] in relative_values:
                     class_probability *= relative_values[new_sample[i]]
                 else:
                     class_probability= 0
                 results[cls] = class_probability
    return results

#calculating total accuracy on the test sample
def get_acc(actual, predicted):
    right = 0.0
    for i in range(len(actual)):
        if predicted[i] == actual[i]:
            right += 1
    return right / len(actual)

#main
def main():
    fulldataset=[]
    features=[]
    testsample=[]
    with open('Q2-tennis.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        """ assuming sunny whether is better and rainy is worst""" 
        """ assuming hot whether is worst and rainy is better"""
        """ assuming non humid whether is better and humid is worst"""                
        """ assuming non windy whether is better and windy is worst"""

        for row in readCSV:
            temp = []
            dataset=[]
            if row[0]=='sunny':
                temp.append(2)
                dataset.append(2)
            elif row[0]=='overcast':
                temp.append(1)
                dataset.append(1)
            elif row[0]=='rainy':
                dataset.append(0)
                temp.append(0)  
            if row[1]=='hot':
                dataset.append(0)
                temp.append(0)
            elif row[1]=='mild':
                dataset.append(1)
                temp.append(1)
            elif row[1]=='cool':
                dataset.append(2)
                temp.append(2)
            if row[2]=='high':
                dataset.append(0)
                temp.append(0)
            elif row[2]=='normal':
                dataset.append(1)
                temp.append(1) 
            if row[3].strip()=='false':
                dataset.append(1)
                temp.append(1)
            elif row[3].strip()=='true':
                dataset.append(0)
                temp.append(0)
            if len(temp) != 0:
                features.append(temp)
            
            if row[4]== 'yes':
                dataset.append(1)
                outcome.append(1)
            elif row[4]=='no':
                dataset.append(0)
                outcome.append(0)
            
                #features.append(temp)
            if len(dataset)!=0:
                fulldataset.append(dataset)
    
    
    newset=np.asarray(features)
    tot_outcomes=0
    for i in newset.T:
        tot_outcomes+=len(set(i.tolist()))
    splitRatio = 0.67
    dataset = fulldataset
    trainingSet, testSet = splitDataset(fulldataset, splitRatio)
    
    lf=int(raw_input('enter smoothning factor:: '))
    predicted = []
    test = []
    
    for t in testSet:
        test.append(t[4])

    for k in range(len(testSet)):
        testsample.append(testSet[k])
        #print ('probaliti of sample{0} being in the particular class is ').format(k)
        results = naive_bayes(trainingSet, outcome, testsample, tot_outcomes, lf)
        #print results
        print('\n\n\n')
        if results[0] > results[1]:
            predicted.append(0)
        else:
            predicted.append(1)
    class_probabilities = occurrences(outcome)
    print ('prior probability of each class')
    print class_probabilities 
    print "Accuracy on test data: ", get_acc(test, predicted)
    
       

main()
    
    
    