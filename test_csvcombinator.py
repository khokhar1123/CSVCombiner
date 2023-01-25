import unittest
import csv
import csvcombinator
import os


class TestCombineCsvs(unittest.TestCase):
    def test_combine_csv_twofiles(self):
        # Create test CSV files
        with open('test1.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('1,2,3\n')
            f.write('4,5,6\n')
        with open('test2.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('7,8,9\n')
            f.write('10,11,12\n')

        csvcombinator.csv_combiner(['test1.csv', 'test2.csv'])

        with open('combined.csv') as f:
            contents = f.read()
            self.assertEqual(
                contents, 'col1,col2,col3,file name\n1,2,3,test1.csv\n4,5,6,test1.csv\n7,8,9,test2.csv\n10,11,12,test2.csv\n')
        os.remove('test1.csv')
        os.remove('test2.csv')
        os.remove('combined.csv')

    def test_combine_csv_three_files(self):
        # Create test CSV files
        with open('test1.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('1,2,3\n')
            f.write('4,5,6\n')
        with open('test2.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('7,8,9\n')
            f.write('10,11,12\n')
        with open('test3.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('13,14,15\n')
            f.write('16,17,18\n')

        csvcombinator.csv_combiner(['test1.csv', 'test2.csv', 'test3.csv'])

        with open('combined.csv') as f:
            contents = f.read()
            self.assertEqual(
                contents, 'col1,col2,col3,file name\n1,2,3,test1.csv\n4,5,6,test1.csv\n7,8,9,test2.csv\n10,11,12,test2.csv\n13,14,15,test3.csv\n16,17,18,test3.csv\n')
        os.remove('test1.csv')
        os.remove('test2.csv')
        os.remove('test3.csv')
        os.remove('combined.csv')

    def test_combine_csv_three_files_diffHead(self):
        # Create test CSV files
        with open('test1.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('1,2,3\n')
            f.write('4,5,6\n')
        with open('test2.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('7,8,9\n')
            f.write('10,11,12\n')
        with open('test3.csv', 'w') as f:
            f.write('col1,col2,col3,col4\n')
            f.write('13,14,15,16\n')
            f.write('17,18,19,20\n')

        csvcombinator.csv_combiner(['test1.csv', 'test2.csv', 'test3.csv'])

        with open('combined.csv') as f:
            contents = f.read()
            self.assertEqual(
                contents, 'col1,col2,col3,col4,file name\n1,2,3,Null,test1.csv\n4,5,6,Null,test1.csv\n7,8,9,Null,test2.csv\n10,11,12,Null,test2.csv\n13,14,15,16,test3.csv\n17,18,19,20,test3.csv\n')
        os.remove('test1.csv')
        os.remove('test2.csv')
        os.remove('test3.csv')
        os.remove('combined.csv')


if __name__ == '__main__':
    unittest.main()
