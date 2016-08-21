#!/usr/bin/env python3
#  coding:utf-8
"""
### Author: Mogu ###

# environment:
    Python3.5.1
# requirements:

"""
import argparse

class fcpy:
    # Main class of fcpy
    def __init__(self):
        pass

    def main(self):
        self._initArgs()
        self.handleArgs()

    def handleArgs(self):
        ctype = self.args.calculation_type
        header = "CALCULATION\t\t:\t{};".format(self.calc_msg[ctype])
        self.header += header
        print(header)
        
        if None == ctype:
            msg = "\nCAUTION:calculation_type is not set!!\n"
            msg += "CAUTION:choise ['distance','cmap','com']\n"
            msg += "PLEASE: cafepy -h "
            raise CmdLineError(msg)
        
        if "" == ctype:
            self.checkFlags(self.args,'i','o')
            self.anim.start()

        
    def checkFlags(self,args,*flags):
        if 'i' in flags:
            msg = "\nCOUTION: No ouput_file !! ex) cafepy [...] -f input-file"
            self._checkArg(args.inputfile,msg)
            header = "INPUTFILE\t\t:\t{};".format(args.inputfile)
            print(header)
            self.header += header

        if 'o' in flags:
            msg = "\nCOUTION: No input_file !! ex) cafepy [...] -o output-file"
            self._checkArg(args.outputfile,msg)
            header = "OUTPUTFILE\t\t:\t{};".format(args.outputfile)
            print(header)
            self.header += header

    def _initArgs(self):
        message = "Analyzing CafeMol outputs."
        parser = argparse.ArgumentParser(description=message)
        parser.add_argument('command', nargs='?',
                            type=str, choices=['run', 'update'],
                            help='choose calculation type.')
        parser.add_argument('-t', '--ctype', nargs='?',
                            help='You choise calcultion methods.')
        parser.add_argument('-o', '--outputfile', nargs='?',
                            help='output file name [.dat]')
        self.args = parser.parse_args()

        return self.args


if __name__ == "__main__":
    tmp = Fcpy()
    print("Fcpy")
