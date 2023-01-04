import argparse
import sys
import math

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='Enter the first number')
    parser.add_argument('--y', type=float, default=1.0, help='Enter the second number')
    parser.add_argument('--operation', type=str, default='sum', help='Choose an operation to perform \n1.Sum\n2.Sub\n3.Mul\n4.Div\n5.Power')


    args = parser.parse_args()
    sys.stdout.write(str(cal(args)))


def cal(args):
    if args.operation.lower() == 'sum':
        return args.x+ args.y
    elif args.operation.lower() == 'sub':
        return args.x - args.y
    elif args.operation.lower() == 'mul':
        return args.x*args.y
    elif args.operation.lower() == 'div':
        return args.x/args.y
    elif args.operation.lower() == 'power':
        return math.pow(args.x,args.y)

if __name__ == '__main__':
    main()