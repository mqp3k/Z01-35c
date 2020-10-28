import os
import sys
import glob

spacing = '   '
dir_level = '│  '
branch_mid = '├──'
branch_end = '└──'


def list_dir(path, line, isLast=True):
    sub_dirs = glob.glob(f'{path}/*/')
    if isLast:
        line = line + spacing
    else:
        line = line + dir_level

    for dirs in sub_dirs:

        if dirs == dir_level[-1]:
            print(line[:-3] + branch_mid + os.path.basename(dirs.rstrip('\\')) + '/')
            list_dir(dirs, line, True)
        else:
            print(line[:-3] + branch_mid + os.path.basename(dirs.rstrip('\\')) + '/')
            list_dir(dirs, line, False)

        list_files(dirs, line)


def list_files(path, line):
    files = glob.glob(f"{path}\\*.*")
    files_left = len(files)
    for f in files:
        files_left = files_left - 1
        if files_left > 0:
            print(f'{line + branch_mid}{os.path.basename(f)}')
        else:
            print(f'{line + branch_end}{os.path.basename(f)}')


def tree_directory(path):
    isLast = False if len(glob.glob(f'{path}/*/')) > 1 else True
    list_dir(sys.argv[1], '', isLast)


if __name__ == '__main__':
    tree_directory(sys.argv[1])