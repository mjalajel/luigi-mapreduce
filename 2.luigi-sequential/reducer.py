#!/usr/bin/env python2.7

import luigi
from transformer import Transformer

class Reducer(luigi.Task):
    def requires(self):
        return Transformer()

    def output(self):
        return luigi.LocalTarget('3-solved.txt')

    def run(self):
        with open(self.input().fn, 'rb') as myinput, self.output().open('w') as myoutput:
            maximum=0
            for num in myinput:
                maximum = max(maximum, int(num))
            myoutput.write("{}\n".format(maximum))

if __name__ == '__main__':
  luigi.run()
