import numpy as np
import time as time
#run python setup.py build_ext --inplace
a=np.random.randn(1000)
b=np.random.randn(100)
m=len(a)
n=len(b)
t1=time.time()
print np.convolve(a,b)
t2=time.time()
mn_con=np.zeros(m+n-1)
for i in range(m):
    for j in range(n):
        if i+j<m+n-1:
            mn_con[i+j]=mn_con[i+j]+a[i]*b[j]
        else:
            break
print mn_con  
t3=time.time()

from cython_conv import cython_conv
print np.asarray(cython_conv(a,b))
t4=time.time()
print "np.convolve time is", t2-t1, 'sec'
print "my convolve time is", t3-t2, 'sec'
print "my cython convolve time is", t4-t3, 'sec'

# 2D convlution
A=np.random.rand(500,500)
#A=np.ones((5,5))
m1=A.shape[0]
n1=A.shape[1]
B=np.random.rand(200,200)
#B=np.ones((2,2))
m2=B.shape[0]
n2=B.shape[1]
from scipy import signal
t5=time.time()
print signal.convolve2d(A,B)
t6=time.time()
#m2n2_con=np.zeros((m1+m2-1,n1+n2-1));
#for i in range(m1):
#    for j in range(n1):
#        for k in range(m2):
#            for l in range(n2):
#                if i+k<m1+m2-1 and j+l<n1+n2-1:
#                    m2n2_con[i+k, j+l]+=A[i,j]*B[k,l]
#print m2n2_con
t7=time.time()
from cython_conv import cython_conv2D
cc=cython_conv2D(A,B)
print np.asarray(cc)
t8=time.time()
print "2D  scipy.signal.convolve2d time is", t6-t5, 'sec'
print "my 2D convolve time is", t7-t6, 'sec'
print "my 2D cython convolve time is", t8-t7, 'sec'






          