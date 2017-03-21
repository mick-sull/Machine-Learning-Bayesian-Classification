# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:31:40 2016

@author: Michael O Sullivan - R00077764 - DCOM4
"""

import os
import re as re
import math


setOfAllWords = set()

def calProbability(dictOfPosWords,dictOfNegWords):
    probPos = {}
    probNeg = {}
    totalPosWordCount = 0
    totalNegWordCount = 0
    
    for word in dictOfPosWords:
        totalPosWordCount += dictOfPosWords[word]
    
    for word in dictOfNegWords :
         totalNegWordCount += dictOfNegWords[word]
    
    for word in setOfAllWords:
        #The word freq. +1 (for smoothing) divided by the total word count and the total unique words from the setOfAllWords
        probPos[word] = (float(dictOfPosWords[word]+1))/(float(totalPosWordCount+len(setOfAllWords)))
        probNeg[word] = (float(dictOfNegWords[word]+1))/(float(totalNegWordCount+len(setOfAllWords)))        
    return (probPos,probNeg)
    

def getDictionary(path):
    dictionary = {}
    listing = os.listdir(path)
    for eachFile in listing:
        txtFile = open(path+eachFile, "r")        
        str = txtFile.read()      
        str = re.sub('\W+', ' ', str)
        str = re.sub('\d+', ' ', str)
        wordsInFile = str.split()
        for word in wordsInFile:
            setOfAllWords.add(word) 
            if word not in dictionary:
                dictionary[word] = 1
            elif word in dictionary:
                dictionary[word] = dictionary[word] + 1
                    
    return (dictionary)
 
def classify(path, probPosDict, probNegDict):
    listing = os.listdir(path)
    totalPos = 0
    totalNeg = 0
    totalTextfile = 0
    for eachFile in listing:
        txtFile = open(path+eachFile, "r")   
        posRes= 0   
        negRes = 0
        str = txtFile.read()
        str = re.sub('\W+', ' ', str)
        str = re.sub('\d+', ' ', str)
        wordsInFile = str.split()
        for word in wordsInFile:
                if word in setOfAllWords:               
                    posRes =  posRes + math.log(probPosDict[word])
                    negRes =  negRes + math.log(probNegDict[word])
        
        if posRes > negRes:
            totalPos= totalPos +1
        else:
            totalNeg= totalNeg +1
        
        totalTextfile = totalTextfile + 1
    
    print "---------", path, "----------"
    print "Postive:  ", (float(totalPos)/float(totalTextfile)) * 100, "%"
    print "Negitive:  ", (float(totalNeg)/float(totalTextfile)) * 100, "%"
    

def main():
    
    dictPos= getDictionary("LargeIMDB\\pos\\") 
    dictNeg = getDictionary("LargeIMDB\\neg\\") 

    
    for word in setOfAllWords:
        if word not in dictPos:
            dictPos[word] = 0
        if word not in dictNeg:
            dictNeg[word] = 0     
                   
    probabilityPos, probabilityNeg =  calProbability(dictPos, dictNeg)

    classify("smallTest\\pos\\" , probabilityPos, probabilityNeg )
    classify("smallTest\\neg\\" , probabilityPos, probabilityNeg )
 


main()