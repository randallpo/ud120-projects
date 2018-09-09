#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys, platform
from time import time
if platform.system() == 'Windows':
    path = "d:/projects/ud120-projects/tools/"
if platform.system() == 'Linux':
    path = "/home/randall/projects/ud120-projects/tools/"
sys.path.append(path)

from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
word_data = path + "word_data.pkl"
email_authors = path + "email_authors.pkl"
features_train, features_test, labels_train, labels_test = preprocess(word_data,email_authors)




#########################################################
### your code goes here ###
#########################################################
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
 
t0 = time()
print clf.score(features_test, labels_test)
print "predictions time:", round(time()-t0, 3), "s"
 

#########################################################
# training time: 2.595 s
# predictions time: 2.595 s
# accuracy: 0.9732650739476678
#########################################################
