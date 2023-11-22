from joblib import Parallel, delayed
import numpy as np
class List(list):
    @staticmethod
    def find_the_max(array):
        l = 0
        arr = []
        for i in array:
            if l == (m:=len(i)):
                arr.append(i)
            if l < m:
                arr = [i]
                l = m
        return (l,arr)
        
    def max_str(self):
        cores = 8
        data = np.array_split(self,8)
        data = Parallel(n_jobs=8)(delayed(self.find_the_max)(i) for i in data)
        l = max(map(lambda x: x[0], data))
        t = sum(map(lambda x: x[1],filter(lambda x: x[0] == l, data)),[])
        return t