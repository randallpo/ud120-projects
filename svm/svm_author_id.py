#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys,platform
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

#########################################################
from sklearn import svm
from sklearn.metrics import accuracy_score
clf = svm.SVC(C=10000, kernel = 'rbf')
t0 = time()
clf.fit(features_train, labels_train)  
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predictions time:", round(time()-t0, 3), "s"
acc = accuracy_score(pred, labels_test)
print "accuracy:", acc

import numpy as np
answer = np.count_nonzero(pred==1)
print "predict Chris {0} times".format(answer)

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
#t0 = time()
#clf.fit(features_train, labels_train)  
#print "small dataset training time:", round(time()-t0, 3), "s"

#t0 = time()
#pred = clf.predict(features_test)
#print "small dataset predictions time:", round(time()-t0, 3), "s"
#acc = accuracy_score(pred, labels_test)
#print "small dataset accuracy:", acc

#answers = [pred[10],pred[26],pred[50]]
#print answers

#########################################################
# kernel: linear
#
# training time: 289.98 s
# predictions time: 34.077 s
# accuracy: 0.984072810011
#
# small dataset training time: 0.173 s
# small dataset predictions time: 2.089 s
# small dataset accuracy: 0.884527872582
#
#########################################################
# kernel: rbf
# C: 1
# small dataset training time: 0.165 s
# small dataset predictions time: 1.803 s
# small dataset accuracy: 0.616040955631
#
# C: 10
# small dataset training time: 0.184 s
# small dataset predictions time: 1.701 s
# small dataset accuracy: 0.616040955631
#
# C: 100
# small dataset training time: 0.187 s
# small dataset predictions time: 1.847 s
# small dataset accuracy: 0.616040955631
#
# C: 1000
# small dataset training time: 0.174 s
# small dataset predictions time: 1.65 s
# small dataset accuracy: 0.821387940842
#
# C: 10000
# training time: 184.106 s
# predictions time: 17.199 s
# accuracy: 0.990898748578
# small dataset training time: 0.183 s
# small dataset predictions time: 1.459 s
# small dataset accuracy: 0.892491467577
#
# [1, 0, 1]
#
# predict Chris 877 times