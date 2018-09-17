#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys, platform
from time import time
if platform.system() == 'Windows':
    path = "d:/projects/ud120-projects/tools/"
if platform.system() == 'Linux':
    path = "/home/randall/projects/ud120-projects/tools/"
if platform.system() == 'Darwin':
    path = "/Users/randallpo/projects/ud120-projects/tools/"
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
from sklearn import tree
from sklearn.metrics import accuracy_score
clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)  
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predictions time:", round(time()-t0, 3), "s"
acc = accuracy_score(pred, labels_test)
print "accuracy:", acc


#########################################################
#
# min_samples_split=40
# training time: 73.523 s
# predictions time: 0.043 s
# accuracy: 0.9761092150170648
#
# 1% of features
# training time: 7.266 s
# predictions time: 0.004 s
# accuracy: 0.9670079635949943
#
#########################################################
