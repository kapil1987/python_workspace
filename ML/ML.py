import numpy as np
import matplotlib.pyplot as plt

def generate_data():
  X = 2*np.random.rand(100,1)
  y = 4 + 3*X + np.random.randn(100,1)
  return X,y
  

def normal_equation():
  X,y = generate_data()
  X_b = np.c_[np.ones((100,1)), X]
  theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
  X_new = np.array([[0], [2]])
  X_new_b = np.c_[np.ones((2,1)), X_new]
  y_predict = X_new_b.dot(theta_best)

  plt.plot(X_new, y_predict, "r-")
  plt.plot(X,y,"b.")
  plt.show()

def gradient_descent(X, Y, m, n):
  """
  Implement gradient descent algo
  
  Parameters
  ----------
  X - numpy 2d array of size mxn. one row is one sample and one column is one feature
  Y - mx1 array of target values
  m - Number of rows in X. Each row represents a sample
  n - number of columns in X. Each column represents a feature

  Returns
  -------
  (n+1)x1 vector of theta
  """
  X_b = np.c_[np.ones((m,1)), X]
  learning_rate = 0.1
  iterations = 1000
  theta = np.random.randn(n+1,1)

  for iteration in range(iterations):
    gradiants = (2/m)*X_b.T.dot(X_b.dot(theta) - Y)
    theta = theta - (learning_rate*gradiants)

  return theta

def test_gradient_descent():
  X,y = generate_data()
  theta = gradient_descent(X,y,100,1)
  X_new = np.array([[0], [2]])
  X_b_new = np.c_[np.ones((2,1)), X_new]
  y_predict = X_b_new.dot(theta)

  plt.plot(X_new, y_predict, "r-")
  plt.plot(X,y, "b.")
  plt.show()

def stochastic_gradient_descent():
  X,y = generate_data()
  X_b = np.c_[np.ones((100,1)), X]
  n_epochs = 50
  theta = np.random.randn(2,1)
  m = 100
  t0,t1 = 5,50

  for epoch in range(n_epochs):
    for i in range(m):
      random_index = np.random.randint(m)
      xi = X_b[random_index:random_index+1]
      yi = y[random_index:random_index+1]

      gradiant = 2*xi.T.dot(xi.dot(theta) - yi)
      learning_schedule = t0/((epoch*m + i) + t1)
      theta = theta - (learning_schedule*gradiant)

  X_new = np.array([[0], [2]])
  X_b_new = np.c_[np.ones((2,1)), X_new]
  y_predict = X_b_new.dot(theta)

  plt.plot(X_new, y_predict, "r-")
  plt.plot(X,y, "b.")
  plt.show()


if __name__ == "__main__":
 # normal_equation()
 #  stochastic_gradient_descent()
 test_gradient_descent()


