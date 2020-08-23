import sys, os
import argparse
from Parser import fileParser, folderParser
from CodeWriter import codewriter

argparser = argparse.ArgumentParser(description='''Convert a single VM file or 
                                                  a directory of VM files to a 
                                                  Hack Assembly Code file (.asm). '''
                                    )

argparser.add_argument('--file', '-f', 
                        type=str, 
                        required=False, 
                        help='Convert a single VM file.'
                        )

argparser.add_argument('--directory', '-d', 
                        type=str, 
                        required=False, 
                        help='Convert a directory of VM files.'
                        )

argparser.add_argument('--bootstrap', 
                        action='store_true', 
                        help='Add the bootstrap code to the .asm file.'
                        )

args = argparser.parse_args()

if args.file is not None:
    input_path = args.file
    output_path = input_path.split('/')[:-1]
    vm_code = fileParser(input_path)

elif args.directory is not None:
    input_path = args.directory
    output_path = input_path.split('/')
    vm_code = folderParser(input_path)

assembly_code = codewriter(input_path, vm_code, args.bootstrap, output_path)