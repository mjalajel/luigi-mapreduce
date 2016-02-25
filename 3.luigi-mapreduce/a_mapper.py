#!/usr/bin/env python2.7
import luigi
import math

class Mapper(luigi.Task):
    infile = luigi.Parameter(always_in_help=True)
    factor = luigi.IntParameter()

    def output(self):
        outputs=[]
        for i in xrange(self.factor):
            fname='a-part-{0:02d}.txt'.format(i)
            #print 'MYLOG -- defined {} as output'.format(fname)
            out = luigi.LocalTarget(fname)
            outputs.append(out)

        #print 'MYLOG -- defined', len(outputs), 'outputs'
        return outputs

    def run(self):
        count_outputs = len(self.output())
        max_index = count_outputs - 1
        #get count line in input file
        num_lines = sum( 1 for line in open(self.infile, 'rb') )
        bulk_size = int( math.ceil(float(num_lines) / self.factor) )

        #split file into FACTOR files
        with open(self.infile, 'rb') as myinput:
            index=0
            myoutput = self.output()[index].open('w')
            line_num=float(0)
            for line in myinput:
                #refresh output, if needed
                #print 'MYLOG -- (line_num={} / bulk_size={})={} > index={} (of {} indices)'.format( line_num, bulk_size, int(line_num / bulk_size), index, max_index)
                if int(line_num / bulk_size) > index:
                    myoutput.close()
                    index += 1
                    #print 'MYLOG -- resetting output to file#{} / {} total outputs'.format(index, count_outputs)
                    myoutput = self.output()[index].open('w')
                #print 'MYLOG -- line#{} directed to file#{}'.format(line_num, index)
                myoutput.write(line)
                line_num += 1
            myoutput.close()

        for i in xrange(index+1, self.factor):
            with self.output()[i].open('w') as emptyout:
                pass

if __name__ == '__main__':
  luigi.run()
