def euclidean(x_train,x_test):
    euc=0
    for i in range(len(x_train)):
        euc=euc+((x_train[i]-x_test[i])**2)
    return euc**0.5
def squared_euclidean(x_train,x_test):
    euc=0
    for i in range(len(x_train)):
        euc=euc+((x_train[i]-x_test[i])**2)
    return euc
def manhattan(x_train,x_test):
    man=0
    for i in range(len(x_train)):
        man=man+abs(x_train[i]-x_test[i])
    return man
def canberra(x_train,x_test):
    cam=0
    for i in range(len(x_train)):
        cam=cam+(abs(x_train[i]-x_test[i])/abs(x_train[i]+x_test[i]))
    return cam
def chebyshev(x_train,x_test):
    cheb=-999
    for i in range(len(x_train)):
        cheb=max(cheb,abs(x_train[i]-x_test[i]))
    return cheb
def bray_curtis(x_train,x_test):
    upper=0
    lower=0
    for i in range(len(x_train)):
        upper=upper+abs(x_train[i]-x_test[i])
        lower=lower+(x_train[i]+x_test[i])
    return upper/lower
