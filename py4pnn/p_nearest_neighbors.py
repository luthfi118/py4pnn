from py4pnn.distance import *

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
        n_class = list(set(t_train))
        nearest_dis = []
        for c in range(len(n_class)):
            dis_cpy = dis.copy()
            t_train_cpy = t_train.copy()
            for i in range(len(dis_cpy)):
                for j in range(len(dis_cpy)-i-1):
                    if(dis_cpy[j]>dis_cpy[j+1]):
                        dis_cpy[j],dis_cpy[j+1]=dis_cpy[j+1],dis_cpy[j]
                        t_train_cpy[j],t_train_cpy[j+1]=t_train_cpy[j+1],t_train_cpy[j]
            temp = []
            for i in range(len(t_train)):
                if(t_train[i]==n_class[c]):
                    temp.append(dis[i])
            nearest_dis.append(temp[:k])
        return nearest_dis, n_class

    def __voting(self,t):
        dis, target = t
        total_dis = []
        prediction = 0
        total_dis = 999
        for i in range(len(target)):
            temp = sum(dis[i])
            if(total_dis>temp):
                total_dis = temp
                prediction = target[i]
        return prediction

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
