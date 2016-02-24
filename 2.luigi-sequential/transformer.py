#!/usr/bin/env python2.7

import luigi
import csv

from mapper import Mapper

class Transformer(luigi.Task):
    def requires(self):
        return Mapper()

    def output(self):
        return luigi.LocalTarget('2-transformed.txt')

    def run(self):
        with open(self.input().fn, 'rb') as myinput, self.output().open('w') as myoutput:
            csvreader = csv.reader(myinput)
            for num,_,_ in csvreader:
                myoutput.write(num)
                myoutput.write('\n')

if __name__ == '__main__':
  luigi.run()
