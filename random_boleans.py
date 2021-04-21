import numpy as np
import random

def l(dim1=100, dim2=100):
  '''this function creates two lists respecting the constraint:
    - true list 
    -false list
    '''
    lista=list()
    t =0
    f =0
    while len(lista)< dim1*dim2:
        if t<(dim1*dim2)*70/100:
            lista.append(1)
            t+=1
        elif f<(dim1*dim2)*30/100:
            lista.append(0)
            f+=1
    return lista

def mix(lista, dim1, dim2):
  '''this function shuffle the elements of a list '''
    contenitore=[]
    dim=dim1*dim2
    for el in range(dim):
        n=random.choice(lista)
        contenitore.append(n)
    return contenitore

def arr(l, dim1=100, dim2=100):
  '''this function creates a numpy array of a desired dimension given a list'''
    array=np.array(l, dtype=bool)
    array=array.reshape((dim1,dim2))
    return array

def _iter(array, dim1, dim2):
  '''this function gives the list of rows having true elements '''
    t = list()
    i = 0
    for i in range(dim1):
        riga = 0
        for j in range(dim2):
            if array[i,j] ==True:
                riga +=1
        t.append(riga)
    t_ = []
    for i in range(len(t)):
        if t[i] == dim1:
            t_.append(t[i])
    return t_, max(t)

def main():
    di=100
    da=100
    a=l(di,da)
    b=mix(a,di,da)
    c=arr(b, di,da)
    m=_iter(c, di,da)
    print(m)

if __name__=='__main__':
    main()
