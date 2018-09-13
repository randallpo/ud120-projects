#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import platform
from time import time
if platform.system() == 'Windows':
    dataset = "d:/projects/ud120-projects/final_project/final_project_dataset.pkl"
if platform.system() == 'Linux':
    dataset = "/home/randall/projects/ud120-projects/final_project/final_project_dataset.pkl"
if platform.system() == 'Darwin':
    dataset = "/Users/randallpo/projects/ud120-projects/final_project/final_project_dataset.pkl"

import pickle
enron_data = pickle.load(open(dataset, "r"))
persons = ["SKILLING JEFFREY K", "LAY KENNETH L","FASTOW ANDREW S"]
n_size = len(enron_data)
n_feature = len(enron_data[persons[0]])
n_poi, n_salary, n_email, money, no_payment, no_poi = 0, 0, 0, 0, 0, 0
for key in enron_data.keys():
    if enron_data[key]["poi"]:
        n_poi += 1
    if enron_data[key]["salary"] != "NaN":
        n_salary += 1
    if enron_data[key]["email_address"] != "NaN":
        n_email += 1
    if enron_data[key]["total_payments"] == "NaN":
        no_payment += 1
    if enron_data[key]["poi"] == "NaN":
        no_poi += 1
p_payment = (no_payment * 100) / n_size
p_poi = (no_poi * 100) / n_size

for person in persons:
    if enron_data[person]["total_payments"] > money:
        money =  enron_data[person]["total_payments"]
        who = person

print "How many data points (people) are in the dataset?: ", n_size
print "For each person, how many features are available? ", n_feature
print "How many POIs are there in the E+F dataset?: ", n_poi
print "How many POIs were there total?: ", 35
print "What is the total value of the stock belonging to James Prentice? ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "How many email messages do we have from Wesley Colwell to persons of interest? ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "What is the value of stock options exercised by Jeffrey K Skilling? %r"% enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "Of these three individuals (Lay, Skilling and Fastow), who took home the most money? (%r, %r)"% (who,money)
print "How many folks in this dataset have a quantified salary? What about a known email address? (%r, %r)"% (n_salary, n_email)
print "How many people in the E+F dataset have 'NaN' for their total payments? ", no_payment
print "What percentage of people in the dataset as a whole is this? ", p_payment
print "How many POIs in the E+F dataset have 'NaN' for their total payments? ", no_poi
print "What percentage of POIs as a whole is this? ", p_poi