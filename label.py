import sys
from tools.helper import *

def main(argv):
    Helper.initialize()
    Helper.something()   

if __name__ == '__main__':
    main(sys.argv[1:])