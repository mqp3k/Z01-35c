import glob
import sys
import os

if len(sys.argv) == 3:
    files = glob.glob("{}\\*.{}".format(sys.argv[1].rstrip('\\'), sys.argv[2].lstrip('.')))
elif len(sys.argv) == 2:
    files = glob.glob("{}\\*".format(sys.argv[1].rstrip('\\')))
else:
    files = glob.glob('.')


for f in files:
    print(os.path.basename(f))