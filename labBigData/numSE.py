from mrjob.job import MRJob

class NumSE(MRJob):
  def mapper(self, _, line):
    idemp,sececon,salary,year = line.split(',')
    yield sececon, 1

  def reducer(self, sector, values):
    yield sector, sum(values)

if __name__ == '__main__':
  NumSE.run()