##!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import platform
if platform.system() == 'Windows':
    path = "d:/projects/ud120-projects/tools/"
    dataset = "d:/projects/ud120-projects/final_project/final_project_dataset.pkl"
if platform.system() == 'Linux':
    path = "/home/randall/projects/ud120-projects/tools/"
    dataset = "/home/randall/projects/ud120-projects/final_project/final_project_dataset.pkl"
if platform.system() == 'Darwin':
    path = "/Users/randallpo/projects/ud120-projects/tools"
    dataset = "/Users/randallpo/projects/ud120-projects/final_project/final_project_dataset.pkl"
sys.path.append(path)

from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open(dataset, "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


## your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

print "Remove TOTAL salary (%r)"% data_dict['TOTAL']['salary']
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

for key in data_dict.keys():
    if data_dict[key]['salary'] != 'NaN':
        if data_dict[key]['salary'] > 1000000 and data_dict[key]['bonus'] > 5000000:
            print "Key [%r] Salary [%r] Bonus[%r]"% (key, data_dict[key]['salary'],data_dict[key]['bonus'])
