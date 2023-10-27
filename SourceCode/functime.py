import time

def timeit(func):
    def i(*args,**kwargs):
        startTime=time.time()
        res=func(*args,**kwargs)
        endTime=time.time()
        print(f'Runing time: {endTime-startTime}')
        return res
    return i