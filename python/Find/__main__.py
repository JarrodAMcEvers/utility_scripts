import argparse
from Find import *
def parseArgs():
	parser = argparse.ArgumentParser(
		description='A Python script that searches directories/filenames for a given pattern and prints out the filepath. Recursively goes through all directories from starting location.'
	)
	parser.add_argument(
		'search',
		type=str,
		help='Pattern to search for in filenames/directories.',
		default=None
	)
	parser.add_argument(
		'directory',
		nargs='?',
		help='Directory to search. Uses current directory by default.',
		default='.'
	)

	return vars(parser.parse_args())

if __name__ == '__main__':
	commandLineArgs = parseArgs()
	find = Find(commandLineArgs['search'], commandLineArgs['directory'])	
	find.find(find.getFilepath())