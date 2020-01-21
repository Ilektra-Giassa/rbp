import sys


def get_input_file(args):
    """
    Return an input file handle
    """
    if args.input_file == "-":
        filehandle = sys.stdin
    else:
        filehandle = open(args.input_file, "r")
    return filehandle


def get_output_file(args):
    """
    Return an output file handle
    """
    if args.output_file == "-":
        filehandle = sys.stdout
    else:
        filehandle = open(args.output_file, "w")
    return filehandle
