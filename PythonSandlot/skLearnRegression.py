import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

from mpl_toolkits.mplot3d import axes3d

''' Get only 2 points in 2d space (0, 0) and (1, 1))
    Equation of line passing thru these 2 points is
    y = x 
    
    Lets see what the sklearn linear model givs us!
    '''
train_data = np.array([[0], [1]])
target = np.array([0,1])

test_data = np.array([[2], [3], [4], [5]])

regr = linear_model.LinearRegression()

regr.fit(train_data, target)
prediction = regr.predict(test_data)

print("coefficient is :", regr.coef_)

''' Plot test_data vs prediction '''

plt.figure(1)
plt.scatter(test_data, prediction)
plt.plot(test_data, prediction, color='blue')
plt.show()

'''
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