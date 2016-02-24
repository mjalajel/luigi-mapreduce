#!/usr/bin/env python2.7
#run: ./generator.py -f dataset.csv -n 100

import csv
import random
import argparse
import string
chars = [char for char in string.ascii_lowercase]

parser = argparse.ArgumentParser(description='user daily frofiles')
parser.add_argument("-f", "--outfile", dest="outfile", help="Output file", required=True )
parser.add_argument("-n", "--samples-count", dest="nsamples", help="Number of samples to generate", required=True, type=int)
args = parser.parse_args()

with open(args.outfile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for _ in xrange(args.nsamples):
        random.shuffle(chars)
        record = [
            random.randint(0, 99999),
            chars[0],
            random.randint(0, 99999)
        ]
        csvwriter.writerow(record)
