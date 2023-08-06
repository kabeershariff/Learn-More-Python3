import argparse
import glob

def all_files():
    files = glob.glob('./**/*.*', recursive=True)
    return files

def all_dirs():
    dirs = glob.glob('./**/', recursive=True)
    return dirs

def find(print_find, name_find, type_find, exec_find, get_all_files, get_all_dirs):
    if print_find and not name_find and not type_find and not exec_find:
        result = sorted(get_all_dirs() + get_all_files())
        print('\n'.join(result))

    if name_find and not type_find and not exec_find:
        file = glob.glob(name_find)
        sub_files = glob.glob(f'{name_find}/*')
        result = sorted(file + sub_files)
        if result:
            print('\n'.join(result))
        else:
            print(f'find: \'{name_find}\': No such file or directory') 

    if type_find and not name_find and not exec_find:
        if type_find == 'f':
            result = get_all_files()
            print('\n'.join(result))
        elif type_find == 'd':
            result = get_all_dirs()
            print('\n'.join(result))
        else:
            print("Invalid type")

    if exec_find and not name_find and not type_find:
        pass


parser = argparse.ArgumentParser(description='Clone of find tool')

parser.add_argument('-print', action='store_true', help='print files')
parser.add_argument('-name', help='name of file to search')
parser.add_argument('-type', help='type of file to search')
parser.add_argument('-exec', help='execute commands')

args = parser.parse_args()

print_find = args.print
name_find = args.name
type_find = args.type
exec_find = args.exec

find(print_find, name_find, type_find, exec_find, all_files, all_dirs)
