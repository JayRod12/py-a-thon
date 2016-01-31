import os
import argparse
import csv



parser = argparse.ArgumentParser(description='Agilent 8642 Signal Generation and Oscilloscope Measurement')

parser.add_argument('--fg', type=str, default='Agilent 8642 A',
                    help='Function Generator')
parser.add_argument('--osc', type=str, default='Agilent blablabla',
                    help='Oscilloscope')
parser.add_argument('--path', type=str, default='files/',
                    help='Path to save files')
parser.add_argument('--o', type=str, default='test',
                    help='Output filename')
parser.add_argument('--startfreq', type=float, nargs=1, default=10000000,
                    help='start frequency of the signal')
parser.add_argument('--endfreq', type=float, nargs=1, default=1000000000,
                    help='end frequency of the signal')
parser.add_argument('--amplitude', type=float, nargs=1, default=2,
                    help='Voltage Peak-To-Peak')
parser.add_argument('--dcoffset', type=float, nargs=1, default=0,
                    help='DC Offset')
args = parser.parse_args()


def measurement(a,b,c,d):
  return

res = [[1,2,3,4], [5,6,7,8]]
measurement(args.startfreq, args.endfreq, args.amplitude, args.dcoffset)

if not os.path.exists(os.path.dirname(args.path)):
    try:
        os.makedirs(os.path.dirname(args.path))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(args.path + args.o, "w") as f:
  writer = csv.writer(f)
  writer.writerows(res)




