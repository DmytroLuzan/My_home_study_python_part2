import os


def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root, dirs, files)
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        #print(root, files, level)
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{sub_indent} {file}')

read_dir('folder')

# tree = os.walk('folder')
# for files in tree:
#     print(tree)






