#!/usr/bin/env python2.7

import luigi
from c_reducer import Reducer

class Collector(luigi.Task):
    factor = luigi.IntParameter(always_in_help=True)
    def requires(self):
        deps=[]
        for i in xrange(self.factor):
            dep = Reducer(myid=i, factor=self.factor)
            deps.append(dep)
        return deps

    def output(self):
        fname='d-solution.txt'
        return luigi.LocalTarget(fname)

    def run(self):
        maximum=0
        for taskinput in self.input():
            with open(taskinput.fn) as f:
                num = f.readline()
                maximum=max(maximum, int(num))

        with self.output().open('w') as myoutput:
            myoutput.write("{}\n".format(maximum))

if __name__ == '__main__':
  luigi.run()
