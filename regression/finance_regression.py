#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys,platform
from time import time
if platform.system() == 'Windows':
    path = "d:/projects/ud120-projects/tools/"
    dataset = "d:/projects/ud120-projects/final_project/final_project_dataset_modified.pkl"
if platform.system() == 'Linux':
    path = "/home/randall/projects/ud120-projects/tools/"
    dataset = "/home/randall/projects/ud120-projects/final_project/final_project_dataset_modified.pkl"
if platform.system() == 'Darwin':
    path = "/Users/randallpo/projects/ud120-projects/tools/"
    dataset = "/Users/randallpo/projects/ud120-projects/final_project/final_project_dataset_modified.pkl"
sys.path.append(path)

import pickle
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load(open(dataset, "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
#features_list = ["bonus", "long_term_incentive"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(feature_train, target_train)
train_score = reg.score(feature_train, target_train)
test_score = reg.score(feature_test, target_test)






### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")



print "What are the slope and intercept? (%r, %r)"% (reg.coef_, reg.intercept_)
print "What is that score on the training data? %r"% train_score
print "What is that score on the testing data? %r"% test_score


## draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass

reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b") 

plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()

print "What are the new slope and intercept? (%r, %r)"% (reg.coef_, reg.intercept_)
