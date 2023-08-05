import argparse

parser = argparse.ArgumentParser(description="Learn how to parse arguments")

#Arguments that are options , i.e take an argument and set a varible
parser.add_argument('--input', help='File input path')
parser.add_argument('--output', help='File output path')
parser.add_argument('--user', help='User name')

#Arguments that are flags, i.e no extra arg, turns something on/off
parser.add_argument('--debug', action='store_true', help='Turn debug mode on')
parser.add_argument('--verbose', action='store_true', help='More detailed output')
parser.add_argument('--noinfo', action='store_false', help='Turn off default info')

#Positional arguments
parser.add_argument('files', nargs='+', help='Get one or more files')

#Parse argments
args = parser.parse_args()

## Usage

#access values of arguments using 'args.my_argument'


if args.noinfo:
    print("Default info")

if args.user:
    print(f"Hello {args.user}")

if args.input:
    print(f"Input file {args.input}")

if args.output:
    print(f"Output file {args.output}")

if args.debug:
    print("Debug mode on")

if args.verbose:
    print("Verbose mode active")

files = args.files
print(files)
