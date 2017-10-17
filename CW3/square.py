import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
#parser.add_argument("square", type=int, help="display square of a given number")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
#parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count", default=0)
args = parser.parse_args()
answer= args.x**args.y
if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
     print("{}^{} == {}".format(args.x, args.y, answer))
#if args.verbosity >= 2:
#    print("running '{}'".format(__file__))
#if args.verbosity >= 1:
#    print("{}^{} == {}".format(args.x, args.y, answer))
#else:
#    print(answer)
