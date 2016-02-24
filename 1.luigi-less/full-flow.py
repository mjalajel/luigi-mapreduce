#!/usr/bin/env python
import csv

maximest=0
with open('../dataset.csv', 'rb') as f:
    csvreader = csv.reader(f)
    for num, _, _ in csvreader:
        num=int(num)
        maximest=max(maximest, num)
print "max is: ", maximest
