import os

to_convert = {}

def fileParser(filePath):
    vmFile = filePath.split('/')[-1][:-3]
    with open(filePath, 'r') as input_file:
        to_convert[vmFile] = []
        for line in input_file:
            cleaned_line = ''
            line = line.split('\n')
            line = line[0].strip()
            try:
                if line[0] == '/':
                    continue
            except IndexError:
                continue
            for c in line:
                if c == '/':
                    break
                else:
                    cleaned_line += c
            to_convert[vmFile].append(cleaned_line)
    return to_convert

def folderParser(folderPath):
    dirFiles = os.listdir(folderPath)
    vmFiles = [f for f in dirFiles if f[-2:] == 'vm']
    vmFiles.remove('Sys.vm')
    vmFiles.insert(0, 'Sys.vm')

    for vmFile in vmFiles:
        to_convert[vmFile] = []
        with open(os.path.join(folderPath, vmFile), 'r') as input_file:
            for line in input_file:
                cleaned_line = ''
                line = line.split('\n')
                line = line[0].strip()
                try:
                    if line[0] == '/':
                        continue
                except IndexError:
                    continue
                for c in line:
                    if c == '/':
                        break
                    else:
                        cleaned_line += c
                to_convert[vmFile].append(cleaned_line)   
    return to_convert

