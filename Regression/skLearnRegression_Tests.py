import unittest
import skLearnRegression
import numpy as np
from reportlab.platypus.tableofcontents import delta


class skLearnRegressionTests(unittest.TestCase):
    
    ''' Unit-tests for sklearn regression'''
    
    def test_LinearRegression_2DataPoints(self):
        train_data = np.array([[0], [1]])
        target = np.array([0,1])
        
        MSE = skLearnRegression.fnLinearRegression(train_data, target)
        
        self.assertAlmostEqual(0, MSE, delta=1.0E-09, msg='test_LinearRegression_2DataPoints')
        
        
        

if __name__ == '__main__':
    unittest.main()