class myKNN(object):
    def __init__(self):
        pass
    def train(self,X,y):
        """ N= # of samples; X=N x D and y =N x 1 """
        self.X_train=X
        self.Y_train=y
    def pred(self, X,k=1,p=1)    :
        """ N_t= # of test samples; X=N_t x D"""
        import numpy as np
        N_t=X.shape[0] #Size of the test set
        Y_pred=np.zeros((k,N_t))
        for i in range(N_t):
            #Find the distance of the test image from all training images
            d=np.sum(np.abs((self.X_train-X[i,:]))**p,axis=1) 
            #Select k nearest images
            k_nns=np.argsort(d)[0:k]
            #Outout k-labes corresponding to the k nearest images
            Y_pred[:,i]=np.round(np.mean(self.Y_train[k_nns]))
        return Y_pred

def unpickle(file):
    import cPickle
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict
        
import numpy as np
#from sklearn.datasets import load_digits
#data=load_digits(n_class=10, return_X_y=True)
load_data=unpickle('cifar_batch1')
X=load_data['data'] #1000x3072 array (1000 images with 32*32*3 pixcels)
Y=np.array(load_data['labels'])
np.random.seed(9525)
test_ind=np.random.choice(np.shape(X)[0], size=100,replace=False)
train_ind=[i for i in range(np.shape(X)[0]) if i not in test_ind]    
X_train=X[train_ind,:]
Y_train=Y[train_ind]
X_test=X[test_ind,:]
Y_test=Y[test_ind]
knn=myKNN()
knn.train(X_train,Y_train)
Y_pred=knn.pred(X_test,1,1)        
print np.mean(Y_pred==Y_test)