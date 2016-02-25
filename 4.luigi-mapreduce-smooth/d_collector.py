#!/usr/bin/env python2.7

import luigi
from a_mapper import Mapper
from c_reducer import Reducer

class Collector(luigi.Task):
    slaves = luigi.IntParameter()
    infile = luigi.Parameter()
    factor = luigi.IntParameter()

    def requires(self):
        deps={
            'mapper': Mapper(infile=self.infile, factor=self.factor),
            'reducers': []
        }
        for i in xrange(self.slaves):
            dep = Reducer(i)
            deps['reducers'].append(dep)
        return deps

    def output(self):
        fname='d-solution.txt'
        return luigi.LocalTarget(fname)

    def run(self):
        maximum=0
        for taskinput in self.input()['reducers']:
            with open(taskinput.fn) as f:
                num = f.readline()
                maximum=max(maximum, int(num))

        with self.output().open('w') as myoutput:
            myoutput.write("{}\n".format(maximum))

if __name__ == '__main__':
  luigi.run()
