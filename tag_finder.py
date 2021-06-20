import os

# TODO: c++
# TODO: save to a file

def find_tag(f_path, name):
    with open(f_path) as f:
        lines = f.readlines()
        for l in lines:
            if l.startswith('# tag: '):
                print(name, l[7:].strip().split(','))

cur_dir = os.getcwd()
# r=root, d=directories, f = files
for r, d, f in os.walk(cur_dir):
    for file in f:
        if file.endswith('.py'):
            find_tag(os.path.join(r, file), file.split('.py')[0])