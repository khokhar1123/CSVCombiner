Mohammad Umar. This is my submission for the task

It is a csv combinator. It has two additonal csv files file1.csv and file2.csv that are used for testing pruposes.

This combinator combines the csv files as described in the writeup. When there are different number of columns it handles that by adding "Null" in the final combined file. For the files that dont have a column it will add "Null"

3 unittests are added in the file test_csvcombinator.py. The test cases are for two simple file merge, 3 files merge, merging of files with different columns.

The main solution is in csvcombinator.py file. Please feel free to contact me if there are any issues running or accessing my submission.

This is how the program can run from command line (file names can be different in name, order , quantity): python csvcombinator.py accessories.csv clothing.csv household_cleaners.csv

Similarly the unittests can be run in the following manner from command line (or directly from ide/console): python test_csvcombinator.py
