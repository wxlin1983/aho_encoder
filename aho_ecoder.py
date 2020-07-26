
import sys
import argparse
import os.path

if sys.version_info < (3, 6):
    raise SystemExit('This code won\'t work on Python 2.x and was not tested on Python 3.5 or before')

parser = argparse.ArgumentParser()
parser.add_argument('in_file', nargs=1, type=str, help='input file')
parser.add_argument('out_file', nargs='?', type=str, help='output file', default = None)
args = parser.parse_args()

fin = args.in_file[0]
if not args.out_file:
    fout = fin + '.out'
else:
    fout = args.out_file

if not os.path.isfile(fin):
    raise FileExistsError('Input file does not exist')

with open(fin, "rb") as f1:
    with open(fout, "wb") as f2:
        x = f1.read(1024)
        while len(x) != 0:
            res = []
            for b in x:
                res.append(255-b)
            res = bytes(bytearray(res))
            f2.write(res)
            x = f1.read(1024)
