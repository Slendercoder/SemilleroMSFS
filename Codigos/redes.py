# Libreria para creacion de redes

from numpy import random
import sys
# from triangular import Triangular

def random_graph(N, p):
    ## Create a random conectivity matrix in which each edge is included with
    ## probability p (Erdos-Renyi model).

    # print(type(N))
    #
    # print('---------')
    # print('Parametros recibidos:', N, p)
    # print('---------')

    #Link counter
    lnkcnt = [0 for i in range(N)]

    ###Link matrix
    ##links = Triangular(N)

    #link list
    llinks = []

    #make the links
    for i in range(N-1):
        for j in range(i+1,N):
            pair = [min(i,j),max(i,j)]
            if random.random() < p:
                lnkcnt[i] += 1
                lnkcnt[j] += 1
                #print(pair)
                #	    links.set_element(i,j,1)
                llinks.append(pair)

    # print(lnkcnt)
    # print(float(sum(lnkcnt))/N)

    ff = open('connlist.dat', 'w')
    for i in range(len(llinks)):
        # print("printing link")
        ff.write(str(llinks[i][0])+" "+str(llinks[i][1])+"\n")
    ff.close()

    #histogram
    hist = [0 for i in range(N)]
    for i in lnkcnt:
        hist[i] += 1

    hf = open('deg_hist.dat', 'w')
    for i in range(N):
        hf.write(str(i)+' '+str(hist[i])+'\n')
    hf.close()
