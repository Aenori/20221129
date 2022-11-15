import re
import traceback
import numpy as np

print_re = re.compile( "\n[ \t]*print *\(" )

def test_with_expected( test_f, f, args, expected ):
    if not isinstance( args, tuple ):
        args = (args,)
    try:
        res = f( *args )
    except Exception as e:
        test_f.fail( "L'appel de votre fonction a échoué avec les arguments {0} et l'exception {1}\n{2}".format(args, e, traceback.format_exc() ) ) 
    test_f.assertEqual( res, expected, "Avec {0} en entrée, votre fonction devrait renvoyer {1}, elle a renvoyé {2}".format(args, expected, res) )

def warning_on_print( In ):
    if print_re.search( In[-1] ):
        print( "="*46 )
        print( " WARNING : vous n'avez pas besoin de print " )
        print( "="*46 )

def check_fonction_in_code( test_f, function_name, In ):
    if not function_name in In[-1]:
        test_f.fail( """Erreur : l'énoncé précisait que vous deviez utilisez la fonction "{0}", elle n'est pas présente dans le code""".format( function_name ) )

def verify_matrix( test_f, global_dict, var_name, matrix_ref ):
    if not var_name in global_dict:
        test_f.fail( "L'énoncé vous demandait de définir une variable {0} qui n'existe pas".format( var_name ) )
    matrix = global_dict[ var_name ]

    if not isinstance( matrix, np.ndarray ):
        test_f.fail( "La variable {0} doit être de type np.array. Elle est de type {1}".format( var_name, type( matrix ) ) )

    if len( matrix.shape ) != len( matrix_ref.shape ):
        test_f.fail( "La variable {0} n'a pas le bon nombre de dimension ! Elle doit en avoir {1}, elle en a {2}".format( var_name, len(matrix_ref.shape), len( matrix.shape ) ) )

    if matrix.shape != matrix_ref.shape:
        test_f.fail( "La variable {0} n'a pas le bon nombre de lignes et de colonnes ! Sa forme devrait être {1}, elle est {2}".format( var_name, matrix_ref.shape, matrix.shape ) )

    test_f.assertTrue( (matrix == matrix_ref).all(), "La forme de la matrice est correcte, mais ces éléments ne correspondent pas à ce qui était attendu" )

def check_mandatory_function( test_f, In, func_name ):
    if not func_name + "(" in In[-1]:
        test_f.fail( "Vous devez utilisez la fonction.méthode {0}. Voir l'énoncé si besoin.".format(func_name) )

