# Understanding argparse - https://doc.python.org/3/howto/argparse.html
# Argparse functions - docs.python.org/3/library/argparse.html#module-argparse
import argparse

# 1. Simple example that does nothing

#parser = argparse.ArgumentParser()
#parser.parse_args()

# 2. Introducing a positional argument

#parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
#args = parser.parse_args()
#print(args.echo)

# 3. Introducing a positional argument with some functionality

#parser = argparse.ArgumentParser()
#parser.add_argument("square", help="displays the square of the number", type=int)
#args = parser.parse_args()
#square_number = args.square**2
#print(square_number)

# 4. Introducing a optional argument 

# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity", action='store_true')
# args = parser.parse_args()
# if args.verbosity:
#    print("verbosity turned on")
    

# 5. Introducing a optional argument - short options

#parser = argparse.ArgumentParser()
#parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
#args = parser.parse_args()
#if args.verbose:
#    print("verbosity turned on")

# 6. Combining positional and optional arguments

#parser = argparse.ArgumentParser()
#parser.add_argument("square", type=int, help="Displays the square of the given number")
#parser.add_argument("-v","--verbose",action="store_true", help="increase output verbosity")
#args = parser.parse_args()
#answer = args.square**2
#if args.verbose:
#    print("The square of {} = {}".format(args.square, answer))
#else:
#    print(answer)
    

# 7. Combining positional and optional arguments - increasing verbosity options

#parser = argparse.ArgumentParser()
#parser.add_argument("square", type=int, help="Displays the square of the given number")
#parser.add_argument("-v","--verbose", choices=['low','high','extreme'], help="increase output verbosity")
#args = parser.parse_args()
#answer = args.square**2

#if args.verbose == 'extreme':
#    print("The square of {} equals {}".format(args.square, answer))
#elif args.verbose == 'high':
#    print("{}**2 = {}".format(args.square, answer))
#else:
#    print(answer)

# 8. Getting a little bit more advanced:

#parser = argparse.ArgumentParser()
#parser.add_argument("x", type=int, help="base")
#parser.add_argument("y", type=int, help="exponent")
#parser.add_argument("-v","--verbose", choices=['low','high','extreme'], help="increase output verbosity")
#args = parser.parse_args()
#answer = args.x**args.y

#if args.verbose == 'high':
    #print('{}^{}={}'.format(args.x, args.y, answer))
#elif args.verbose == 'extreme':
    #print('Base ({})^Exponent ({}) = {}'.format(args.x, args.y, answer))
#else:
    #print(answer)

# 9. Adding mutually exclusive group
    
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose", action="store_true")
group.add_argument("-q","--quiet", action="store_true")
parser.add_argument("x", type=int, help="base")
parser.add_argument("y", type=int, help="exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print('{}^{}={}'.format(args.x, args.y, answer))
elif args.verbose:
    print('Base ({})^Exponent ({}) = {}'.format(args.x, args.y, answer))
else:
    print(answer)

