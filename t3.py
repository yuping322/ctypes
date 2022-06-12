import time
from ctypes import *
def fbnqslb(shu,l):
    print()
    i = 0
    if(shu == 0):
        return l 
    else:
        if(len(l)-1 <= 0):
            l.append(1)
        else:
            l.append(l[len(l)-1]+l[len(l)-2])
        return fbnqslb(shu-1,l)
def fbnqslnb(x):
    if (x <= 2):
        return 1          
    else:
        return fbnqslnb(x-2)+fbnqslnb(x-1)   
start_time = time.time()         
c1 = fbnqslb(40,[])
end_time = time.time()
print("time1: {}".format(end_time - start_time))
start_time = time.time()
c2 = fbnqslnb(40)
end_time = time.time()
print("time2: {}".format(end_time - start_time))
print(c1)         
print(c2)        

start_time = time.time()
so_obj = cdll.LoadLibrary("./libfb.so.0")
int_arg = c_int(40)
rest = so_obj.fb(int_arg)
end_time = time.time()
print("time3: {}".format(end_time - start_time))
print(rest)
