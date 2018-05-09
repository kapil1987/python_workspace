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
        
        MSE, coefficients, intercept = skLearnRegression.fnLinearRegression(train_data, target, title)
        
        ''' coefficients here is going to be a 1D array with 1 element since there is only
            one feature in training data '''
        
        self.assertAlmostEqual(0, MSE, delta=1.0E-09, msg='test_LinearRegression_2DataPoints')
        self.assertAlmostEqual(1, coefficients[0], delta=1.0E-09, msg='test_LinearRegression_2DataPoints : coefficient error')
        self.assertAlmostEqual(0, intercept, delta=1.0E-09, msg='test_LinearRegression_2DataPoints : intercept error')
        
    
    ''' 3 data points 
        1. train data = column vector [0,1,2]
        2. target = [0,1,3]
        
        Linear regression should give the straight line y = (3/2)x-(1/6) '''
    def test_LinearRegression_3DataPoints(self):
        train_data = np.array([[0],[1],[2]])
        target = np.array([0,1,3])
        
        title = 'test_LinearRegression_3DataPoints'
        MSE, coefficients, intercept = skLearnRegression.fnLinearRegression(train_data, target, title)
        
        ExpectedMSE = 1/18 # Calculated
        
        self.assertAlmostEqual(1.5, coefficients[0], delta=1.0E-09,msg='test_LinearRegression_3DataPoints : coefficients error')
        self.assertAlmostEqual(-(1/6), intercept, delta=1.0E-09, msg='test_LinearRegression_3DataPoints : intercept error')
        self.assertAlmostEqual(ExpectedMSE, MSE, delta=1.0E-09, msg = 'test_LinearRegression_3DataPoints : MSE error')
        
        

if __name__ == '__main__':
    unittest.main()