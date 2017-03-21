# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:31:40 2016

@author: micha
"""

import os
from pandas import * 
import matplotlib.pyplot as plt
import numpy as np
import re as re
import math
from nltk.corpus import stopwords
setOfAllWords = set()
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup

vectorizer = CountVectorizer(stop_words='english')
stopWords = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

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
        #                       The word freq. +1 (for smoothing) divided by the total word count and the total unique words from the setOfAllWords
        probPos[word] = (float(dictOfPosWords[word]+1))/(float(totalPosWordCount+len(setOfAllWords)))
        probNeg[word] = (float(dictOfNegWords[word]+1))/(float(totalNegWordCount+len(setOfAllWords)))        
    return (probPos,probNeg)
    

def getDictionary(path):
    dictionary = {}
    listing = os.listdir(path)
    for eachFile in listing:
        txtFile = open(path+eachFile, "r")
        
        txtFile = BeautifulSoup(txtFile) 
        
        str = txtFile.get_text()   
        str = re.sub('\W+', ' ', str)
        str = re.sub('\d+', ' ', str)
        wordsInFile = str.split()
        for word in wordsInFile:
            word = stemmer.stem(word)
            word = word.lower()
            if word not in stopWords:
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
        txtFile = BeautifulSoup(txtFile) 
        posRes= 0   
        negRes = 0
        str = txtFile.get_text()   
        #str = re.sub("[^a-zA-Z]", ' ', str)
        str = re.sub('\W+', ' ', str)
        str = re.sub('\d+', ' ', str)
        wordsInFile = str.split()
        for word in wordsInFile:
            word = stemmer.stem(word)
            word = word.lower()
            if word not in stopWords:
                if word in setOfAllWords:               
                    posRes =  posRes + math.log(probPosDict[word])
                    #print "posRes", posRes + math.log(probPosDict[word])
                    negRes =  negRes + math.log(probNegDict[word])
                    #print "negRes", negRes + math.log(probNegDict[word])
        
        if posRes > negRes:
            #print "Positives"
            totalPos= totalPos +1
        else:
            #print "Negitive"
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
 
    print "2dictNeg", len(dictNeg)
    print "2dictPos", len(dictPos)
    print "2set len setOfAllWords ", len(setOfAllWords)

main()