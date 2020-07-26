
import sys
import argparse
import os.path

if sys.version_info < (3, 0):
    raise SystemExit(
        'This code won\'t work on Python 2.x.')

parser = argparse.ArgumentParser()
parser.add_argument('in_file', nargs=1, type=str, help='input file')
parser.add_argument('out_file', nargs='?', type=str,
                    help='output file', default=None)
args = parser.parse_args()

fin = args.in_file[0]
if not os.path.isfile(fin):
    raise FileExistsError('Input file does not exist')

if not args.out_file:
    fout = fin + '.out'
else:
    fout = args.out_file


def f(n):
    return 255 - n


with open(fin, "rb") as f1:
    with open(fout, "wb") as f2:
        x = f1.read(1024)
        while len(x) != 0:
            res = bytearray(list(map(f, x)))
            f2.write(res)
            x = f1.read(1024)
