import argparse
from selectFunctions import *

parser = argparse.ArgumentParser(prog = 'shipviewer', description="Hello World")
parser.add_argument('action', action="store")
parser.add_argument('-n', action="store")
parser.add_argument('-c', action="store")

args = vars(parser.parse_args())

if args['action'] == "show" and args['n'] is not None:
    selectByName(args['n'])

if args['action'] == "show" and args['c'] is not None:
    selectByCode(str(args['c']))

if args['action'] == "search" and args['n'] is not None:
    filterByName(args['n'])

if args['action'] == "status" and args['n'] is not None:
    selectJourneys(args['n'])