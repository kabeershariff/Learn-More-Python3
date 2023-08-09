from os.path import exists
import argparse 
import re

class Main(object):
    def grep(self, file, pattern):
        if exists(file):                                    #check if file exists
            with open(file, 'r') as text:                   #'with' keyword properly closes files after operation
                for i, line in enumerate(text, start=1):    #enumeration func to iterate over the string line by line
                    match = re.search(pattern, line)        #search the input string for a match
                    if match:
                        print(f"Line {i} :{match.group()}") #instead of printing whole object #group() only returns the matched data
        else:
            print("Invalid/File not found")
    

parser = argparse.ArgumentParser(description='A Stupid clone of grep tool.')    #Learning is never Stupid

parser.add_argument('file', help='File to be searched.')
parser.add_argument('pattern', help='search pattern.')

args = parser.parse_args()

file = args.file
pattern = args.pattern

Main().grep(file, pattern)

