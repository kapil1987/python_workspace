import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.metrics import r2_score

from mpl_toolkits.mplot3d import axes3d
from sklearn.metrics.regression import mean_squared_error
from code import interact



'''\fn \fnLinearRegression(train_data, target)
   
   \brief train sklearn linear regression with the given
   train data. Plot following

   1. Find out prediction with train data itself
   2. Scatter plot of train_data vs target
   3. Plot of train_data vs prediction 
   
   \returns mean squared error between target and prediction. Regression coefficients
            ,intercept and r2 score
   '''
   
def fnLinearRegression(TrainData, Target, Title):
    
    regr = linear_model.LinearRegression()
    regr.fit(TrainData, Target)
    
    prediction = regr.predict(TrainData)
    
    plt.figure(1)
    
    plt.title(Title)
    plt.scatter(TrainData, Target)
    plt.plot(TrainData, prediction, color = 'blue')
    
    plt.show()
    
    ''' Find out mean sqs uared error between prediction and target '''
    
    MSE = mean_squared_error(Target, prediction)
    
    R2_Score = r2_score(Target, prediction)
    
    return MSE, regr.coef_, regr.intercept_, R2_Score 

''' Get only 2 points in 2d space (0, 0) and (1, 1))
    Equation of line passing thru these 2 points is
    y = x 
    
    Lets see what the sklearn linear model givs us!
train_data = np.array([[0], [1]])
target = np.array([0,1])

test_data = np.array([[2], [3], [4], [5]])

regr = linear_model.LinearRegression()

regr.fit(train_data, target)
prediction = regr.predict(test_data)

print("coefficient is :", regr.coef_)
print("Mean squared error", mean_squared_error(test_data, prediction))


plt.figure(1)
plt.scatter(test_data, prediction)
plt.plot(test_data, prediction, color='blue')
plt.show()


data_x = np.array([0,1,2])
data_y = np.array([0,1,2])
data_z = np.array([0,1,2])

fig = plt.figure(1)

ax = axes3d.Axes3D(fig)


ax.scatter(data_x, data_y, data_z)

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

ax.set_zlim(0,2)
plt.show()
'''