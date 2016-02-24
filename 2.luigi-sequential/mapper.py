#!/usr/bin/env python2.7
import luigi

class Mapper(luigi.Task):
    infile = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget('1-part.txt')

    def run(self):
        with open(self.infile, 'rb') as myinput, self.output().open('w') as myoutput:
            for line in myinput:
                myoutput.write(line)

if __name__ == '__main__':
  luigi.run()
