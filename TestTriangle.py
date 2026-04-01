# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    #----------- Right Triangles -----------
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right Triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right Triangle')

    #----------- Equilateral Triangles -----------
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral Triangle')

    #----------- Isosceles Triangles -----------
    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(5,5,3),'Isosceles','5,5,3 is a Isosceles Triangle')
    
    #----------- Scalene Triangle -----------
    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 is a Scalene Triangle')

    #----------- Not A Triangle -----------
    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is not a Triangle')

    #----------- Invalid Input -----------
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(0,5,5),'InvalidInput','That is not a valid input')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(-1,5,5),'InvalidInput','That is not a valid input')
        
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(201,5,5),'InvalidInput','That is not a valid input')
        
    def testInvalidInputD(self): 
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput','That is not a valid input')
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

