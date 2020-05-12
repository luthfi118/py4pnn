from py4knn.distance import *
class pnn:
    def __init__(self):
        pass
    def __distance(self,x_train,x_test,opt):
        dis=[]
        for i in range(len(x_train)):
            if(opt=='euclidean'):
                dis.append(euclidean(x_train[i],x_test))
            elif(opt=='squared_euclidean'):
                dis.append(squared_euclidean(x_train[i],x_test))
            elif(opt=='manhattan'):
                dis.append(manhattan(x_train[i],x_test))
            elif(opt=='canberra'):
                dis.append(canberra(x_train[i],x_test))
            elif(opt=='chebyshev'):
                dis.append(chebyshev(x_train[i],x_test))
            elif(opt=='bray_curtis'):
                dis.append(bray_curtis(x_train[i],x_test))
            else:
                dis.append(euclidean(x_train[i],x_test))
        return dis
    def __sort(self,dis,t_train,k):
        for i in range(len(dis)):
            for j in range(len(dis)-i-1):
                if(dis[j]>dis[j+1]):
                    dis[j],dis[j+1]=dis[j+1],dis[j]
                    t_train[j],t_train[j+1]=t_train[j+1],t_train[j]
        return t_train[:k]
    def __voting(self,t):
        return max(set(t), key=t.count)
    def predict(self,x_train,t_train,x_test,k,opt='euclidean'):
        dis=[]
        sorted_t=[]
        hasil=[]
        try:
            if(k>len(x_train)):
                raise Exception
            for i in range(len(x_test)):
                dis.append(self.__distance(x_train,x_test[i],opt))
            for i in range(len(x_test)):
                sorted_t.append(self.__sort(dis[i],t_train.copy(),k))
            for i in range(len(x_test)):
                hasil.append(self.__voting(sorted_t[i]))
            return hasil
        except:
            pass
