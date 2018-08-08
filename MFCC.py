import librosa
import numpy as np
import os
import pandas as pd


y_all = pd.read_csv('/Users/n/PycharmProjects/wave/data/meta/meta.txt', sep = '\t', header=None)
Y = y_all.iloc[:,4]

directory = '/Users/n/PycharmProjects/wave/data/audio/'
files = os.listdir(directory)
files =files [1: ]

n=[]
print(n)
for i in files:
    y, sr = librosa.load('/Users/n/PycharmProjects/wave/data/audio/' + i )
    m = np.mean(librosa.feature.mfcc(y=y, sr=sr), axis=0)
    #n = np.append(n, [m], axis=0)
    n.append(m)
    #n =  np.vstack((n,m))

y = Y.tolist()

lst = [1,0,0]
a=0
for i in y:
    if i == 'background':
        y[a]=lst
    a=a+1
print (y)








