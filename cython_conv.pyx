import numpy as np
def cython_conv(double[:] a, double[:] b):
    cdef int m=len(a)
    cdef int n=len(b)
    cdef double[:] mn_con=np.zeros(m+n-1)
    cdef int i
    cdef int j
    for i in range(m):
        for j in range(n):
            if i+j<m+n-1:
                mn_con[i+j]=mn_con[i+j]+a[i]*b[j] 
            else:
                break
    return mn_con            
          
            
def cython_conv2D(double[:,:] A, double[:,:] B):
    cdef int m1=A.shape[0]
    cdef int n1=A.shape[1]
    cdef int m2=B.shape[0]
    cdef int n2=B.shape[1]
    
    cdef double[:,:] sol=np.zeros((m1+m2-1,n1+n2-1))
    cdef int i,j,k,l
    for i in range(m1):
        for j in range(n1):
            for k in range(m2):
                for l in range(n2):
                    if i+k<m1+m2-1 and j+l<n1+n2-1:
                        sol[i+k, j+l]+=A[i,j]*B[k,l]
                    else:
                        break
    return sol 
