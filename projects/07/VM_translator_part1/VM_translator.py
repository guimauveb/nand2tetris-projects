import sys
from Parser import parser
from CodeWriter import codewriter

filename = sys.argv[1]

vm_code = parser(filename)
assembly_code = codewriter(filename, vm_code)