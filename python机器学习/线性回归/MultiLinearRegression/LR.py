from numpy import genfromtxt
from sklearn import linear_model

# Set the current directory to the path of the script itself.
import os,sys
os.chdir(os.path.dirname(sys.argv[0]))

dataPath = r"Delivery.csv"
deliveryData = genfromtxt(dataPath,delimiter=',')

print ("data")
print (deliveryData)

x= deliveryData[:,:-1] 
#Extract the data of all rows in all columns except the last column as the x value.

y = deliveryData[:,-1] 
#Extract the data of all rows in the last column as the y value.

print (x)
print (y)

lr = linear_model.LinearRegression()
lr.fit(x, y)

print (lr)
# result:LinearRegression(copy_X=True, \
# fit_intercept=True, n_jobs=None, normalize=False)

print("coefficients:")
print (lr.coef_)

print("intercept:")
print (lr.intercept_)

xPredict = [[102,6],]
yPredict = lr.predict(xPredict)
print("predict:")
print (yPredict)
