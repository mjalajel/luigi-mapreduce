#!/usr/bin/env python2.7

import luigi
from reducer import Reducer

class Collector(luigi.Task):
    slaves = luigi.IntParameter()
    def requires(self):
        deps=[]
        for i in xrange(self.slaves):
            dep = Reducer(i)
            deps.append(dep)
        return deps

    def output(self):
        fname='4.solution.txt'
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
