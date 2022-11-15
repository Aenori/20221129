import unittest
import sys
import traceback
import collections
import re
import random
this = sys.modules[__name__]

import cours_python_utils as cpy_utils
## test_with_expected
## check_fonction_in_code

class TestExercice1Q1( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "ones" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'vector_q1', np.ones(3) )

class TestExercice1Q2( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "zeros" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'vector_q2', np.zeros(5) )

class TestExercice1Q3( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "zeros" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'matrix_q3', np.zeros((3,3)) )

class TestExercice1Q4( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "zeros" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'matrix_q4', np.zeros((2,4)) )

class TestExercice1Q5( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "eye" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'matrix_q5', np.eye(3) )

class TestExercice1Q6( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "eye" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'matrix_q6', np.array( [[1,2,3],[0,1,2],[0,0,1]] ) )

class TestExercice1Q7( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "array" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'vector_q7', np.array( [1,2,3,4] ) )

class TestExercice1Q8( unittest.TestCase ):
    def test_code(self):
        cpy_utils.check_mandatory_function( self, In, "array" )

    def test_fonction(self):
        cpy_utils.verify_matrix( self, globals(), 'matrix_q8', np.array( [[1],[4],[9],[16]] ) )

class TestExercice2( unittest.TestCase ):
    def test_code(self):
        if not ".min(" in In[-1]:
            print("Are you sure you choose the simplest solution ?")

    def test_fonction(self):
        cpy_utils.test_with_expected(self, is_positive, (np.array( [[1],[4],[-9],[16]] ),), False )
        cpy_utils.test_with_expected(self, is_positive, (np.array( [[1],[4],[9],[16]] ),), True )
        cpy_utils.test_with_expected(self, is_positive, (np.array( [[1,1,1],[4,4,4],[9,9,9],[16,16,16]] ),), True )
        cpy_utils.test_with_expected(self, is_positive, (np.array( [[1,1],[4,4],[9,-9],[16,16]] ),), False )

class TestExercice3( unittest.TestCase ):
    def test_fonction(self):
        cpy_utils.test_with_expected(self, calcule_trace, (np.array( [[4]] ),), 4 )
        cpy_utils.test_with_expected(self, calcule_trace, (np.array( [[1,4],[9,16]] ),), 17 )
        cpy_utils.test_with_expected(self, calcule_trace, (np.array( [[-10,1,1],[4,5,4],[9,9,7]] ),), 2 )

class TestExercice4( unittest.TestCase ):
    def test_fonction(self):
        cpy_utils.test_with_expected( self, is_nihilpotent, (np.array( [[0,0,0],[0,0,0],[0,0,0]] ),), True )
        for i in range(3):
            for j in range(3):
                mat = np.zeros((3,3))
                mat[i,j] = 1
                cpy_utils.test_with_expected( self, is_nihilpotent, (mat,), i != j )
        cpy_utils.test_with_expected( self, is_nihilpotent, (np.array( [[0,1,1],[0,0,1],[0,0,0]] ),), True )


class TestExercice5( unittest.TestCase ):
    def test_fonction(self):
        self.assertAlmostEqual(x + 2*y + 3*z,15)
        self.assertAlmostEqual(x + 3*y + 5*z,20)
        self.assertAlmostEqual(x + 4*y -   z,30)

class TestExercice6( unittest.TestCase ):
    def test_fonction(self):
        cpy_utils.test_with_expected( self, est_projecteur, (np.array( [[0,0,0],[0,0,0],[0,0,0]] ),), True )
        for i in range(3):
            for j in range(3):
                mat = np.zeros((3,3))
                mat[i,j] = 1
                cpy_utils.test_with_expected( self, est_projecteur, (mat,), i == j )
        cpy_utils.test_with_expected( self, est_projecteur, (np.array( [[0,1,1],[0,0,1],[0,0,0]] ),), False )

class TestExercice7( unittest.TestCase ):
    def test_fonction(self):
        cpy_utils.test_with_expected( self, est_rotation, (np.array( [[1,0,0],[0,1,0],[0,0,1]] ),), True )
        cpy_utils.test_with_expected( self, est_rotation, (np.array( [[1,0,0],[0,0,1],[0,1,0]] ),), True )
        cpy_utils.test_with_expected( self, est_rotation, (np.array( [[1,0,0],[0,3**0.5/2,1/2],[0,1/2,-3**0.5/2]] ),), True )
        cpy_utils.test_with_expected( self, est_rotation, (np.array( [[1,0,0],[0,1,0],[0,1,1]] ),), False )
        cpy_utils.test_with_expected( self, est_rotation, (np.array( [[0,0,0],[0,0,0],[0,0,0]] ),), False )
        cpy_utils.test_with_expected( self, est_rotation, (np.array( [[1,0,0],[0,1,0],[0,0,2]] ),), False )

def tester_exo( n, globals_dict ):
    for k, v in globals_dict.items():
        setattr( this, k, v )
    launch_test_case( eval( "TestExercice{0}".format(n) ) )

def launch_test_case( test_case ):
  suite = unittest.TestLoader().loadTestsFromTestCase( test_case )
  unittest.TextTestRunner(verbosity=2).run(suite)

