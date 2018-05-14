import unittest
import skLearnRegression
import numpy as np
from code import interact
from reportlab.platypus.tableofcontents import delta



class skLearnRegressionTests(unittest.TestCase):
    
    ''' Unit-tests for sklearn regression'''
    
    def test_LinearRegression_2DataPoints(self):
        train_data = np.array([[0], [1]])
        target = np.array([0,1])
        
        title = 'test_LinearRegression_2DataPoints'
        
        MSE, coefficients, intercept, r2 = skLearnRegression.fnLinearRegression(train_data, target, title)
        
        ''' coefficients here is going to be a 1D array with 1 element since there is only
            one feature in training data '''
        
        self.assertAlmostEqual(0, MSE, delta=1.0E-09, msg='test_LinearRegression_2DataPoints')
        self.assertAlmostEqual(1, coefficients[0], delta=1.0E-09, msg='test_LinearRegression_2DataPoints : coefficient error')
        self.assertAlmostEqual(0, intercept, delta=1.0E-09, msg='test_LinearRegression_2DataPoints : intercept error')
        
        # r2 value should be 1. Line is completely fitting the data points
        
        ''' r2 score - My understanding of r2 score is that it is a measure of how good
            the fitted line is compared to the straight line y = m, where m is the mean
            value of the data points.
    
            1.1. Lets say the values on x axis are {x(0),x(1),......x(n)}.
                 the corresponding values on y axis are {y(0), y(1),.....y(n)}.
                 The mean value of the output values is m.
    
            1.2. The fitted straight line by linear regression model is:
                 b = ax + c
    
            1.3. so the values on the fitted line corresponding to the input will be
                 {b(0), b(1),....b(n)}
    
            1.4. r2 score is calculated as r2 = 1 - (summation((y(i) - b(i))^2)/summation((y(i) - m)^2)).
    
                1.4.1. In this equation, the lower the term - "summation((y(i) - b(i))^2) is, the better the r2
                      score is.
    
                1.4.2. Term - "summation((y(i) - b(i))^2)" is squared error in prediction. So the lower
                       is squared error in prediction the better is the value of r2 score
                       self.assertEqual(1, r2, msg = 'test_LinearRegression_2DataPoints : r2 error')'''
        
        
        # For this test the r2 value should be exactly equal to 1 since there are only 2 data points and
        # the fitted line passes thru these points
        
        
        self.assertEqual(1, r2, msg = 'test_LinearRegression_2DataPoints : r2 error')
        
    
    ''' 3 data points 
        1. train data = column vector [0,1,2]
        2. target = [0,1,3]
        
        Linear regression should give the straight line y = (3/2)x-(1/6) '''
    def test_LinearRegression_3DataPoints(self):
        train_data = np.array([[0],[1],[2]])
        target = np.array([0,1,3])
        
        title = 'test_LinearRegression_3DataPoints'
        MSE, coefficients, intercept, r2 = skLearnRegression.fnLinearRegression(train_data, target, title)
        
        ExpectedMSE = 1/18 # Calculated
        ExpectedR2 = 27/28 # This is calculated mathematically
        
        self.assertAlmostEqual(1.5, coefficients[0], delta=1.0E-09,msg='test_LinearRegression_3DataPoints : coefficients error')
        self.assertAlmostEqual(-(1/6), intercept, delta=1.0E-09, msg='test_LinearRegression_3DataPoints : intercept error')
        self.assertAlmostEqual(ExpectedMSE, MSE, delta=1.0E-09, msg = 'test_LinearRegression_3DataPoints : MSE error')
        self.assertAlmostEqual(ExpectedR2, r2, delta=1.0E-09, msg='test_LinearRegression_3DataPoints: r2 error')
        

if __name__ == '__main__':
    unittest.main()