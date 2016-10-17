#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""

import os
import regression_test


os.chdir( os.getcwd() )

test_dirs = ((os.path.join(os.getcwd(), "../tests/regression_test_samples/cpp"),    ".h"),
             (os.path.join(os.getcwd(), "../tests/regression_test_samples/java"),   ".java"),
             (os.path.join(os.getcwd(), "../tests/regression_test_samples/python"), ".py") )

regression_test.create_log_file( "regression_test.log" )

test_sols = regression_test.parse_solution_file_ex( os.path.join(os.getcwd(), "../tests/test_solutions.log") )

for di in test_dirs:

    regression_test.test_find_variables( di, "regression_test.log", "test_solutions.log", test_sols )

raw_input( "Test completed \nPress Enter to Exit" )
