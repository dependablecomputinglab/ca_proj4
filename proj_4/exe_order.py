#!/usr/bin/python
import sys


def main(argv):
    input_name = argv[1]
    output_name = argv[2]

    try:
        with open(input_name) as inFile:
            for line in inFile:
                stripped = line.strip()
                if len(stripped) < 1 or not stripped[0].isdigit():
                    #blank line or not debug message
                    continue

                tokens = line.split()
                tick = int(tokens[0][:-1])
                debug_flag = tokens[1][:-1]
                message = " ".join(tokens[2:])

                #your code here

    except IOError as e:
        print "error opening file to read: {}".format(input_name)
        exit(1)

    try:
        with open(output_name, "w") as outFile:
            #your code here
            pass

    except IOError as e:
        print "error opening file to write: {}".format(
            output_name)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: exe_order.py <input file name> <output file name>"
        exit(1)
    main(sys.argv)
