import argparse

def cat(files, output_file):
    output = ""
    try:
        for i in files:
            txt = open(i)
            output += txt.read()
    except:
        print("Invalid/missing file")
        quit()
    
    if output_file:
        txt = open(output_file, 'w')
        txt.write(output)
        txt.close()

    else:
        print(output, end='')


parser = argparse.ArgumentParser(description='A bad clone of the cat command')

parser.add_argument('files', nargs='+', help='one or more input files')
parser.add_argument('--output', help='output file name')

args = parser.parse_args()

files = args.files
output = args.output

cat(files, output)
