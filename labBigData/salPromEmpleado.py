from mrjob.job import MRJob

class SalPromEmpleado(MRJob):
  def mapper(self, _, line):
    idemp,sececon,salary,year = line.split(',')
    yield idemp, int(salary)

  def reducer(self, id, values):
    l = list(values)
    res = sum(l)/len(l)
    yield id, res

if __name__ == '__main__':
  SalPromEmpleado.run()