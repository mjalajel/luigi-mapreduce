#!/usr/bin/env python2.7

import luigi
from b_transformer import Transformer

class Reducer(luigi.Task):
    myid   = luigi.IntParameter()
    factor = luigi.IntParameter()

    def requires(self):
        return Transformer(myid=self.myid, factor=self.factor)

    def output(self):
        fname='c-solved-{0:02d}.txt'.format(self.myid)
        return luigi.LocalTarget(fname)

    def run(self):
        with open(self.input().fn, 'rb') as myinput, self.output().open('w') as myoutput:
            maximum=0
            for num in myinput:
                maximum = max(maximum, int(num))
            myoutput.write("{}\n".format(maximum))

if __name__ == '__main__':
  luigi.run()
