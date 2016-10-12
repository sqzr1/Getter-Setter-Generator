#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""

import os
import regression_test


os.chdir( os.getcwd() )

test_dirs = ((os.path.join(os.getcwd(), "Getter Setter Test Files\\TestC++Files"),    ".h"),
             (os.path.join(os.getcwd(), "Getter Setter Test Files\\TestJavaFiles"),   ".java"),
             (os.path.join(os.getcwd(), "Getter Setter Test Files\\TestPythonFiles"), ".py") )

regression_test.create_log_file( "GetterSetterLog.rtf" )

test_sols = regression_test.parse_solution_file_ex( os.getcwd() + "//TestSolutions.rtf" )

for di in test_dirs:

    regression_test.test_find_variables( di, "GetterSetterLog.rtf", "TestSolutions.rtf", test_sols )

raw_input( "Test completed \nPress Enter to Exit" )
