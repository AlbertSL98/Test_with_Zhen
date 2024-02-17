#try
#python parse -i 1 -o 2
import sys
import argparse
command = sys.argv[1:]
print(command)
parser = argparse.ArgumentParser(description="Parses command.")
parser.add_argument("-i", "--input", help="Your input file.")
parser.add_argument("-o", "--output", help="Your destination output file.")
#options = parser.parse_args(['-i', '1', '-o', '2'])
options = parser.parse_args(command)
print(options)
print(options.input)
print(options.output)

'''
#sys-input will be stored as a list, like the example here
options = parser.parse_args(['-i', '1', '-o', '2'])
#if miss one, then it is None
options = parser.parse_args(['-i', '1'])
options.output == None
'''

'''
#also try this
import sys
import argparse
command = sys.argv[1:]
print(command)
parser = argparse.ArgumentParser(description="Parses command.")
parser.add_argument("-i", "--i", help="Your input file.")
parser.add_argument("-o", "--o", help="Your destination output file.")
#options = parser.parse_args(['-i', '1', '-o', '2'])
options = parser.parse_args(command)
print(options.i)
print(options.o)
'''