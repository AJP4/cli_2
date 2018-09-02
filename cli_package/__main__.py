import argparse
from .classexample import Constants
from .helperfunctions import say_name

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase verbosity", action="store_true")
    parser.add_argument("name",type=str)
    args=parser.parse_args()

    if args.verbose:
        print("verbosity is on")
    else:
        print("terse")

    myconstant=Constants()
    print('Start')
    print('1-', Constants.MYNAME)
    myconstant.say()
    say_name(args.name)
    print('End')



if __name__ == '__main__':
    main()