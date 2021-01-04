#!/usr/bin/env python3
from matplotlib import pyplot as plt
from numpy import sin, cos, arange, pi
Xcol = 0
Ycol = []
Ycols = []
X = []
Y = []
NUMS = 0
with open("data.csv", "r") as data_file:
    for i,line in enumerate(data_file.read().split("\n")):
        if(i>0 and not line==""):
            X.append(float(line.split(",")[Xcol]))
            for i in range(len(Ycol)):
                Y[i].append(float(line.split(",")[Ycol[i]]))
        elif(i==0):
            cols = line.split(",")
            print(cols)
            Xcols = input("What is the independent column? ")
            Xcol = cols.index(Xcols)
            NUMS = int(input("How many dependent variables? "))
            for i in range(NUMS):
                Ycols.append(input("What is the dependent column? "))
                Ycol.append(cols.index(Ycols[-1]))
            Y = [[] for i in range(NUMS)]
for i in range(len(Ycol)):
    plt.plot(X, Y[i])
plt.legend(Ycols)
plt.savefig("image.png")
