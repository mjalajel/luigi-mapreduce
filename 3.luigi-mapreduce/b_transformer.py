#!/usr/bin/env python2.7

import luigi
import csv

from a_mapper import Mapper

class Transformer(luigi.Task):
    myid   = luigi.IntParameter()
    factor = luigi.IntParameter()

    def requires(self):
        return Mapper(factor=self.factor)

    def output(self):
        fname='b-transformed-{0:02d}.txt'.format(self.myid)
        return luigi.LocalTarget(fname)

    def run(self):
        with open(self.input()[self.myid].fn, 'rb') as myinput, self.output().open('w') as myoutput:
            csvreader = csv.reader(myinput)
            for num,_,_ in csvreader:
                myoutput.write(num)
                myoutput.write('\n')

if __name__ == '__main__':
  luigi.run()
